
扩展包
- selenium                  web自动化测试扩展
- pytest-html               pytest自带的报表
- pytest-xdist              多线程测试
- allure-pytest             美化版报表
  - python -m pytest -sv --alluredir ./temp   生成文件
  - allure generate ./temp -o ./report --clean
- pytest-ordering           用于改变测试用例的执行顺序 
- pytest-rerunfailures      用例失败后重新执行
- pytest-dependency         用例之间的依赖关系
