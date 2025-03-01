import logging
from datetime import datetime
from odoo import http, _
from odoo.http import request

_logger = logging.getLogger(__name__)


class StockBarcodeController(http.Controller):

    @http.route('/qr_code_scanner/scan_from_main_menu', type='json', auth='user')
    def main_menu(self, barcode, **kw):
        """
        Receive a barcode scanned from the main menu, extract data, and create a partner record
        if it does not already exist.
        """
        try:
            # Convert barcode data to a dictionary
            data_dict = self._parse_barcode_data(barcode)
            _logger.info("Parsed Barcode Data: %s", data_dict)

            # Check if partner with the given ID already exists
            partner_exists = request.env['res.partner'].sudo().search(
                [('nic_id', '=', data_dict['ID'])])

            if partner_exists:
                return {'warning': _('ID Already Exists: %(ID)s with name %(name)s') % {
                    'ID': data_dict['ID'], 'name': partner_exists.name}}

            # Create new partner record
            new_partner = self._create_partner_record(data_dict)
            _logger.info("New Partner Created: ID %s", new_partner.id)

            return {'partner_id': new_partner.id, 'message': 'Partner created successfully'}

        except Exception as e:
            _logger.error("Error processing barcode: %s", str(e))
            return {'error': _('An error occurred while processing the barcode.')}

    def _parse_barcode_data(self, barcode_data):
        """
        Parses the barcode data into a dictionary format.
        """
        lines = barcode_data.split('\n')
        data_dict = {}
        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                data_dict[parts[0].strip()] = parts[1].strip()
        return data_dict

    def _create_partner_record(self, data_dict):
        """
        Creates a new res.partner record from barcode data.
        """
        date_format = '%d/%m/%Y'
        return request.env['res.partner'].sudo().create({
            'nic_id': data_dict['ID'],
            'name': data_dict['Full name'],
            'province_name': data_dict['Province'],
            'issue_province': data_dict['Issue Province'],
            'marital_status': data_dict['Marital status'],
            'gender': 'Feminine' if data_dict['Sex'].title()[0] == 'F' else 'Masculine',
            'issue_date': datetime.strptime(data_dict['ID issue date'], date_format),
            'exp_date': datetime.strptime(data_dict['ID Exp date'], date_format),
        })
