# coding=utf-8
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import quote
import sys
import time

class Main:
	def index(self,keyboard,i):
		# splice send request link.
		link="https://www.liepin.com/zhaopin/?key=" + quote(keyboard) + "&currentPage="+str(i)
		# request headers information.
		headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0"}
		# send request.
		req=urllib.request.Request(link,headers=headers)
		# get response information.
		response = urllib.request.urlopen(req)
		# set utf-8 format to prevent garbled code.
		html = response.read().decode("utf-8")
		# process relevant web page data with beautifulsoup.
		soup=BeautifulSoup(html,'html.parser')
		# get the class where the data we need, including job title, working years and other information.
		sojob_result=soup.find("div",class_='left-list-box')
		
		list=sojob_result.find_all("li")
		# job info
		for x in range(0,len(list)):
			if list[x].find("div", class_='job-title-box') is not None:
		   	  	# job name
				job_name=list[x].find("div", class_='job-title-box').find("div", class_='ellipsis-1').get_text().strip()

				# require
				requirement = ""
				labels_tags=list[x].find_all("span", class_='labels-tag')
				for y in range(0, len(labels_tags)):
					requirement += labels_tags[y].get_text().strip()
					if y < len(labels_tags):
						requirement += ","

				# work place
				work_city=list[x].find("div", class_='job-title-box').find("span", class_='ellipsis-1').get_text().strip()

				# whether to hire urhently
				hot = 1
				if list[x].find("div", class_='job-tag') is not None:
					hot =1
				else:
					hot = 0

				# salary
				salary_down = "negotiable"
				salary_up = "negotiable"
				# year-end awards
				final_wage="None"
				job_salary=list[x].find("span", class_='job-salary').get_text().strip()
				if "·" in job_salary:
					final_wage=job_salary.split("·")[1]
					job_salary=job_salary.split("·")[0]
				if "-" in job_salary:
					salary_down=float(job_salary.split("-")[0])*1000
					salary_up=float(job_salary.split("-")[1].strip("k"))*1000

				# company name
				company_name=list[x].find("span", class_='company-name').get_text().strip()

				# company tags
				company_tags=list[x].find("div", class_='company-tags-box ellipsis-1').find_all("span")
				# industry
				industry = company_tags[0].get_text().strip()
				# company status
				company_status = "undisclosed"
				if len(company_tags) == 3:
					company_status = company_tags[1].get_text().strip()
				# company size
				company_size = company_tags[len(company_tags) - 1].get_text().strip()
				# outprint
				print("job_name: {0}, requirement: {1} work_city: {2}, hot: {3}, salary: {4} - {5}, year-end_awards: {6}, company_name: {7}, industry: {8}, company_status: {9}, company_size: {10}".format(job_name, requirement, work_city, hot, salary_down, salary_up, final_wage, company_name, industry, company_status, company_size))

if __name__=="__main__":
	keyboard = sys.argv[1]
	pages = sys.argv[2]
	for page in range(0,int(1)):
		Main().index(keyboard,pages);