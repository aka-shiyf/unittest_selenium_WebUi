import unittest
from HTMLTestRunner import HTMLTestRunner
from unittestreport import TestRunner
from common.excel_util import ExcelUtil
from mail.send_mail import SendMail

if __name__ == '__main__':
    # 使用unittest默认的测试用例的加载器去发现testcase目录下所有py结尾的测试用例
    # suite = unittest.defaultTestLoader.discover("./testcase", "*.py")
    # # 生成html报告文件
    # report_file = open(ExcelUtil().get_object_path() + "report/report.html", "w", encoding='utf-8')
    # # 生成一个HTMLTestRunner运行器对象（必须下载一个HTMLTestRunner.py文件，放到python的lin目录）
    # runner = HTMLTestRunner.HTMLTestRunner(stream=report_file, title="自动化测试报告", description="测试情况如下：")
    # runner.run(suite)
    suite = unittest.TestLoader().discover("./testcase", "*.py")
    run = TestRunner(suite, tester='石大大', filename="report1.html", report_dir=ExcelUtil().get_object_path() + 'report',
                     title='UI自动化测试报告', desc='登录功能自动化测试', templates=2)

    run.run()
    SendMail().send_mail()
