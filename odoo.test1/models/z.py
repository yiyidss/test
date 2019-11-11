# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_test(models.Model):
    _name = "my_test"
    _description = u"系统参数设置"
    _rec_name = 'name'

    num = fields.Integer(string = "数量")
    date = fields.Date(string = "日期")
    name = fields.Char(string='名称')
    dtl = fields.One2many('my_test1','guanlian',string='人员')
    sex = fields.Selection([('1','男'),('2','女'),('3','萝莉')],string='性别')
    bool = fields.Boolean(string='勾选')


    @api.multi
    def say(self):
        print(self.id,self.num,self.sex)
        R = self.env['my_test1'].search([('id','<',3)])
        R.id = 1
        self.num=13
        for i in R:
            if  i.id == 1:
                i.name='壹原侑子'
            else:
                i.name='四月一日'

        # R.name='柚子'


