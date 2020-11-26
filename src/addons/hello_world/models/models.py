# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *

class hello_world(models.Model):
    _name = 'hello_world.hello_world'
    _description = 'This is a sample model for the hello_world module.'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

class glucose_measurement(models.Model):
    _name = 'hellow_world.glucose_measurement'
    _description = 'This represents a point in time measurement of glucose.'

    timestamp = fields.Datetime(string='Date & Time', required=True, index=True, default=datetime.now(), copy=False)
    glucose = fields.Integer(string='Glucose (mg/dL)', required=True)
    
