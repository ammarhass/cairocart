from odoo import models, fields, api, _


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    def open_partner_ledger(self):
        self.ensure_one()
        return {
            'name': "Partner Ledger",
            'type': 'ir.actions.client',
            'tag': 'p_l',
            'params': {
                'active_id': self.id
                # 'options': {'partner_id': self.id},
                # 'ignore_session': 'both',
            },
            'context': self._context
        }
