# -*- coding: UTF-8 -*-

import os
import re


dir = input("请输入图片所在目录：").strip()

while not os.path.exists(dir):
	dir = input("目录不存在，请重新输入：").strip()

dir = re.escape(dir)

quality = 90
resizeW = 0
resizeH = 0


def main():
	image_list = os.listdir(dir+'/')
	if not os.path.exists(dir+'/webp'):
		os.mkdir(dir+'/webp')
	for image_name in image_list:
		image_name = re.escape(image_name)
		pathFrom = '{}/{}'.format(dir, image_name)
		pathTo = '{}/webp/{}'.format(dir, image_name.replace('png', 'webp'))
		os.system('cwebp -q {q} -resize {w} {h} {pf} -o {pt}'.format(
			q=quality,
			w=resizeW,
			h=resizeH,
			pf=pathFrom,
			pt=pathTo
		))

if __name__ == '__main__':
    main()