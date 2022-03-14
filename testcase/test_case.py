from ddt import ddt, data, unpack
from base.base_util import BaseUtil
from common.excel_util import ExcelUtil
from pageobject.login_page import LoginPage


@ddt
class TestCase(BaseUtil):

    @unpack  # 数据过多的情况下可直接对返回列表进行取值再做处理
    @data(*ExcelUtil().read_excel())  # *解包，调用返回解包后的列表数据
    def test_03_login(self,index,username, password, code):
        """
        用户登录测试用例
        :param index: 数据据序号
        :param username: 用户名
        :param password: 密码
        :param code: 验证码
        :return:
        """

        lp = LoginPage(self.dr)
        lp.login_ecshop(username, password, code)
