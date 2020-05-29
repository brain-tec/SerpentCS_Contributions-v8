# See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class BusinessCategory(models.Model):
    _name = 'business.category'

    name = fields.Char('Name')


class Relation(models.Model):
    _name = 'relation.relation'

    name = fields.Char('Name')
