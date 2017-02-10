# -*- coding: utf-8 -*-
'''
@author: CQ
'''
import os, sys, re, json
reload(sys)
#sys.setdefaultencoding('utf8')
sys.setdefaultencoding('gbk')

def curDir():
	#运行目录
	#CurrentPath = os.getcwd()
	#return CurrentPath
	#当前脚本
	#return sys.argv[0]
	#当前脚本目录
	ScriptPath = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
	return ScriptPath

#获取文件夹下的文件
def getFilelist(dir) :
    path = dir
    filelist = []
    files = os.listdir(path)
    for f in files :
        if(f[0] == '.') :
            pass
        if os.path.isfile(f):
            pass
        else :
            filelist.append(f)
    return filelist

#解析map文件中的坐标
_reg = r'(?=\"name\":).+?(?<=],)'
def cities(value):
	pattern = re.compile(_reg)
	_list = pattern.findall(value)
	if _list:
		for l in _list:
			l = '{'+l.decode('utf8')+'},'
			yield l
			
	

_mapdir = 'echarts-maps'
def main():
	coordinate = '[';
	path = os.path.join(curDir(), _mapdir);
	allfile = getFilelist(path)
	for f in allfile :
		fp = open(os.path.join(path, f))
		fname = f.replace('.json', '')
		
		coordinate += '{"province": "'+ fname + '", "cities": ' + '['
		
		try:
			json = fp.read()
		finally:
			fp.close()
		for city in cities(json):
			coordinate += city
		
		coordinate += ']}'
	coordinate += ']'
	
	print coordinate
	
if __name__ == '__main__':
	main()
