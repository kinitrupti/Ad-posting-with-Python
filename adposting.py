#open gedit/texteditor/notepad
import mechanize #open terminal and type : sudo pip install python-mechanize
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
title = "Travel/Tourism Marketing"
description = "Dear Reader,We, At xyz, Are Looking For Individuals Who Can Promote Our Business (Only On Internet) In Travel & Tourism (Part Time/Full Time) & Provide Customer Service To People Across India. xyz Is An ISO Certified Entity Listed On Ministry Of Corporate Affairs. Our Company Provides Best-In-Class Service In The Travel & Tourism Sector Across World. Besides This, xyz Envisions Providing Income Opportunity To Those People Who Are Passionate To Fulfill Their Dreams. Earn 10000 To 12000 Per Week This Position Is Open For People In Service/Business/College. Even Retired/Housewives/Fresher Can Join Us. Kindly Call Us Now. Email:"
companyname = "xyz Pvt. Ltd."
place = "Mumbai"
salary = "INR10,000 per week"
br = mechanize.Browser() #initiating a browser

br.set_handle_robots(False) #ignore robots.txt

br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

gitbot = br.open("https://www.example.com") #requesting the website base url

br.select_form(nr=3) #the sign up form in website is in third position

br["PostJob1$JobTitle"] = title #right click and inspect element on the ad posting page. PostJob1$JobTitle is the name attribute of title field

br["PostJob1$CompanyName"] = companyname 

br["PostJob1$JobDescription"] = description 
br["PostJob1$LocationInputMap1$l"] = place 
br["PostJob1$Salary"] = salary 
response = br.response()
response.read()
sign_up = br.submit()
