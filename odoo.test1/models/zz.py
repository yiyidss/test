# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_test1(models.Model):
    _name = "my_test1"
    _description = u"系统参数设置"

    id = fields.Char(string = "id")
    name=fields.Char(string="名称")
    num = fields.Integer(string = "数量")
    jiage=fields.Integer(string='价格')
    date = fields.Date(string = "日期")
    guanlian = fields.Many2one('my_test',string='部门')
    a = fields.Integer(related='guanlian.num',string='部门的数量')
    b = fields.Date(related='guanlian.date',string='部门的日期')