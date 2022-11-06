from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import pandas as pd
import datetime
from glob import glob

#Inputs
sheet_id = '11ErZA49kg7mKQ8SzsDy01pws7dOw9WX8cFPheesudl8'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
import datetime
Today = datetime.datetime.now()
data = df[df['Date']==Today.strftime("%d/%m/%Y")]
print(data)
CSM=str(data.iloc[0].CSM)
CP_Name = str(data.iloc[0].CP_Name)
Product_Type = str(data.iloc[0].Product_Type)
Insurer = str(data.iloc[0].Insurer)
Registration_No = str(data.iloc[0].Registration_No)
Insured_Name = str(data.iloc[0].Insured_Name)
Policy_Type = str(data.iloc[0].Policy_Type)
IDV_raw = data.iloc[0].IDV
IDV = str(IDV_raw)
Imt_23 = str(data.iloc[0].Imt_23)
MOP = str(data.iloc[0].MOP)
Premium = str(data.iloc[0].Premium)
Date = str(data.iloc[0].Date)

Business_Type = str(data.iloc[0].Business_Type)
Name_Transfer = str(data.iloc[0].Name_Transfer)
Product_Group = str(data.iloc[0].Product_Group)
Product_Type = str(data.iloc[0].Product_Type)
ISP_Type_Code = str(data.iloc[0].ISP_Type_Code)
Make_and_Model = str(data.iloc[0].Make_and_Model)
Policy_Start_Date_Str = str(data.iloc[0].Policy_Start_Date)
Policy_Start_Date_Date = datetime.datetime.strptime(Policy_Start_Date_Str,"%d/%m/%Y")
Policy_Start_Date = Policy_Start_Date_Date.strftime('%d%m%Y')
NCB = str(data.iloc[0].NCB)
Allocation = str(data.iloc[0].Allocation)
Discount = str(data.iloc[0].Discount)
GVW = str(data.iloc[0].GVW)
CC = str(data.iloc[0].CC)
Hypothecation_There = str(data.iloc[0].Hypothecation_There)
Hypothecation = str(data.iloc[0].Hypothecation)
Prev_Ins_Policy_There = str(data.iloc[0].Prev_Ins_Policy_There)
Prev_Ins_Comp = str(data.iloc[0].Prev_Ins_Comp)
Prev_Policy_Expiry_Date_Str = str(data.iloc[0].Prev_Policy_Expiry_Date)
Prev_Policy_Expiry_Date_Date = datetime.datetime.strptime(Prev_Policy_Expiry_Date_Str,"%d/%m/%Y")
Prev_Policy_Expiry_Date = Prev_Policy_Expiry_Date_Date.strftime('%d%m%Y')

Prev_Policy_Number = str(data.iloc[0].Prev_Policy_Number)
Policy_Number = str(data.iloc[0].Policy_Number)
Year_of_MFG = str(data.iloc[0].Year_of_MFG)
Date_of_Reg_Date_Str = str(data.iloc[0].Date_of_Reg)
Date_of_Reg_Date_Date = datetime.datetime.strptime(Date_of_Reg_Date_Str,"%d/%m/%Y")
Date_of_Reg = Date_of_Reg_Date_Date.strftime('%d%m%Y')
Policy_Start_Date_Str = str(data.iloc[0].Policy_Start_Date)
Policy_Start_Date_Date = datetime.datetime.strptime(Policy_Start_Date_Str,"%d/%m/%Y")
Policy_Start_Date = Policy_Start_Date_Date.strftime('%d%m%Y')
Policy_End_Date_Str = str(data.iloc[0].Policy_End_Date)
Policy_End_Date_Date = datetime.datetime.strptime(Policy_End_Date_Str,"%d/%m/%Y")
Policy_End_Date = Policy_End_Date_Date.strftime('%d%m%Y')
Final_Discount = str(data.iloc[0].Final_Discount)
OD_Premium = str(data.iloc[0].OD_Premium)
TP_Premium = str(data.iloc[0].TP_Premium)
GST = str(data.iloc[0].GST)
Membership_Points = str(data.iloc[0].Membership_Points)
PaymentBy = str(data.iloc[0].PaymentBy)
Vendor_Payment = str(data.iloc[0].Vendor_Payment)


PATH = "F:/Allins period/November"
DATE3 = Today.strftime("%d-%m-%Y")
Path_Location = PATH+"/"+DATE3
Files = glob(Path_Location+"/*")
print(Files)
Files_Data_Frame = pd.DataFrame(Files)
Files_Data = Files_Data_Frame[0].str.replace('\\','/',regex= True)
Files_Data
for i in Files_Data :
    print(i)

#Webdriver
driver = webdriver.Chrome(executable_path="E:\chromedriver_win32\chromedriver.exe")
driver.get("http://erp.allins.in/#/login/login")
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@id='mat-input-0']").send_keys("DHANALAXMI.V")
driver.find_element(By.XPATH,"//*[@id='mat-input-1']").send_keys("January@2001")
driver.find_element(By.XPATH,"/html/body/app-root/div[1]/div[2]/div/div/div/div/div/div/form/button").click()
driver.implicitly_wait(5)
Sales = driver.find_element(By.XPATH,"/html/body/app-dashboard/header/div/div/ul[1]/li[3]/a")
Sales.click()
Order_Verification_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/div/nav/ul/span/span[3]/li[6]/a/span").click()
driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/div/nav/ul/span/span[3]/li[6]/a/span").click()
driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/app-xperts-page/div/div[2]/div[1]/form/div[1]/div/button[1]").click()


## Verification page
Date_2 = Today.strftime("%d%m%Y")
print(Date_2)
# driver.find_element(By.ID,"dtmFromDate").send_keys(Date_2)
# driver.find_element(By.ID,"dtmToDate").send_keys(Date_2)
# time.sleep(3)
# driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/app-xperts-page/div/div[2]/div[1]/form/div[2]/div/div[13]/button[2]").click()
# time.sleep(3)
# driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/app-xperts-page/div/div[3]/div/div[1]/div/div/table/tbody/tr/td[14]/i[2]").click()
# # #
# # driver.implicitly_wait(2)
# # Business_Type_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[1]/ng-select/div/div/div[3]/input")
# # Business_Type_Button.send_keys(Business_Type)
# # Business_Type_Button.send_keys(Keys.ENTER)
# # if (Name_Transfer == "Yes") :
# #     Name_Transfer_Button = driver.find_element(By.XPATH,"//*[@id='mat-checkbox-1']/label/div")
# #     Name_Transfer_Button.click()
# # else:
# #     Name_Transfer_Button= driver.find_element(By.XPATH,"//*[@id='mat-checkbox-1']/label/div")
# #
# # Product_Group_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[6]/ng-select/div/div/div[3]/input")
# # Product_Group_Button.send_keys(Product_Group)
# # Product_Group_Button.send_keys(Keys.ENTER)
# #
# # Product_Type_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[7]/ng-select/div/div/div[3]/input")
# # Product_Type_Button.send_keys(Product_Type)
# # Product_Type_Button.send_keys(Keys.ENTER)
# # driver.implicitly_wait(1)
# # ISP_Type_Code_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[9]/ng-select/div/div/div[3]/input")
# # ISP_Type_Code_Button.send_keys(ISP_Type_Code)
# # ISP_Type_Code_Button.send_keys(Keys.ENTER)
# # Make_and_Model_Button = driver.find_element(By.XPATH,"//*[@id='mat-input-10']")
# # Make_and_Model_Button.send_keys(Make_and_Model)
# # Make_and_Model_Button.send_keys(Keys.ENTER)
# # Policy_Start_Date_Button = driver.find_element(By.XPATH,"//*[@id='mat-input-11']")
# # Policy_Start_Date_Button.send_keys(Policy_Start_Date)
# # NCB_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[16]/ng-select/div/div/div[3]/input")
# # NCB_Button.send_keys(NCB)
# # NCB_Button.send_keys(Keys.ENTER)
# # Allocation_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[17]/ng-select/div/div/div[3]/input")
# # Allocation_Button.send_keys(Allocation)
# # Allocation_Button.send_keys(Keys.ENTER)
# # Discount_Button = driver.find_element(By.XPATH,"//*[@id='mat-input-12']")
# # Discount_Button.send_keys(Discount)
# # GVW_Button = driver.find_element(By.ID,"mat-input-13")
# # GVW_Button.send_keys(Keys.BACKSPACE)
# # GVW_BackSpaced = GVW_Button.send_keys(Keys.BACKSPACE+Keys.BACKSPACE+GVW)
# # CC_Button = driver.find_element(By.ID,"mat-input-14")
# # CC_Button.send_keys(Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+CC)
# # # if (Hypothecation_There == "Yes"):
# # #     Hypothecation_Yes_Button = driver.find_element(By.ID,"mat-checkbox-2")
# # #     Hypothecation_Yes_Button.click()
# # #     Hypothecation_Button = driver.find_element(By.ID,"mat-input-15")
# # #     Hypothecation_Button.send_keys(Hypothecation)
# # #     Hypothecation_Button.send_keys(Keys.ENTER)
# # if(Prev_Ins_Policy_There == "Yes"):
# #     Prev_Ins_Policy_There_Button = driver.find_element(By.ID,"mat-checkbox-3")
# #     Prev_Ins_Policy_There_Button.click()
# #     Prev_Ins_Comp_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[23]/div/div[2]/ng-select/div/div/div[2]/input")
# #     Prev_Ins_Comp_Button.send_keys(Prev_Ins_Comp+Keys.ENTER)
# #     Prev_Policy_Expiry_Date_Button = driver.find_element(By.ID,"mat-input-16")
# #     Prev_Policy_Expiry_Date_Button.send_keys(Prev_Policy_Expiry_Date)
# #     driver.implicitly_wait(1)
# #     Prev_Policy_Number_Button = driver.find_element(By.ID,"mat-input-17")
# #     Prev_Policy_Number_Button.send_keys(Prev_Policy_Number)
# #
# # Authorized_Button = driver.find_element(By.ID,"mat-checkbox-9").click()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
## Verification filling
# driver.implicitly_wait(2)
# Business_Type_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[1]/ng-select/div/div/div[2]/input")
# Business_Type_Button.send_keys(Business_Type)
# Business_Type_Button.send_keys(Keys.ENTER)
# if (Name_Transfer == "Yes") :
#     Name_Transfer_Button = driver.find_element(By.XPATH,"//*[@id='mat-checkbox-1']/label/div")
#     Name_Transfer_Button.click()
# else:
#     Name_Transfer_Button= driver.find_element(By.XPATH,"//*[@id='mat-checkbox-1']/label/div")
#
# Product_Group_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[6]/ng-select/div/div/div[2]/input")
# Product_Group_Button.send_keys(Product_Group)
# Product_Group_Button.send_keys(Keys.ENTER)
#
# Product_Type_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[7]/ng-select/div/div/div[3]/input")
# Product_Type_Button.send_keys(Product_Type)
# Product_Type_Button.send_keys(Keys.ENTER)
# driver.implicitly_wait(1)
# ISP_Type_Code_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[9]/ng-select/div/div/div[2]/input")
# ISP_Type_Code_Button.send_keys(ISP_Type_Code)
# ISP_Type_Code_Button.send_keys(Keys.ENTER)
# Make_and_Model_Button = driver.find_element(By.XPATH,"//*[@id='mat-input-10']")
# Make_and_Model_Button.send_keys(Make_and_Model)
# Make_and_Model_Button.send_keys(Keys.ENTER)
# Policy_Start_Date_Button = driver.find_element(By.XPATH,"//*[@id='mat-input-11']")
# Policy_Start_Date_Button.send_keys(Policy_Start_Date)
# NCB_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[16]/ng-select/div/div/div[3]/input")
# NCB_Button.send_keys(NCB)
# NCB_Button.send_keys(Keys.ENTER)
# Allocation_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[17]/ng-select/div/div/div[3]/input")
# Allocation_Button.send_keys(Allocation)
# Allocation_Button.send_keys(Keys.ENTER)
# Discount_Button = driver.find_element(By.XPATH,"//*[@id='mat-input-12']")
# Discount_Button.send_keys(Discount)
# GVW_Button = driver.find_element(By.ID,"mat-input-13")
# GVW_Button.send_keys(Keys.BACKSPACE)
# GVW_BackSpaced = GVW_Button.send_keys(Keys.BACKSPACE+Keys.BACKSPACE+GVW)
# CC_Button = driver.find_element(By.ID,"mat-input-14")
# CC_Button.send_keys(Keys.BACKSPACE+Keys.BACKSPACE+Keys.BACKSPACE+CC)
# if (Hypothecation_There == "Yes"):
#     Hypothecation_Yes_Button = driver.find_element(By.ID,"mat-checkbox-2")
#     Hypothecation_Yes_Button.click()
#     Hypothecation_Button = driver.find_element(By.ID,"mat-input-15")
#     Hypothecation_Button.send_keys(Hypothecation)
#     Hypothecation_Button.send_keys(Keys.ENTER)
# if(Prev_Ins_Policy_There == "Yes"):
#     Hypothecation_There_Button = driver.find_element(By.ID,"mat-checkbox-3")
#     Hypothecation_There_Button.click()
#     Prev_Ins_Comp_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[2]/div[2]/div[2]/div/div[23]/div/div[2]/ng-select/div/div/div[2]/input")
#     Prev_Ins_Comp_Button.send_keys(Prev_Ins_Comp+Keys.ENTER)
#     Prev_Policy_Expiry_Date_Button = driver.find_element(By.ID,"mat-input-16")
#     Prev_Policy_Expiry_Date_Button.send_keys(Prev_Policy_Expiry_Date)
#     driver.implicitly_wait(1)
#     Prev_Policy_Number_Button = driver.find_element(By.ID,"mat-input-17")
#     Prev_Policy_Number_Button.send_keys(Prev_Policy_Number)
# Authorized_Button = driver.find_element(By.ID,"mat-checkbox-4").click()
# driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-orderverification/div/div/div/form/div/div[3]/div/div/button[2]").click()


## Closure
Order_Closure_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/div/nav/ul/span/span[3]/li[7]/a/span")
Order_Closure_Button.click()
driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/app-xperts-page/div/div[2]/div[1]/form/div[1]/div/button[1]").click()
driver.find_element(By.ID,"dtmFromDate").send_keys(Date_2)
driver.find_element(By.ID,"dtmToDate").send_keys(Date_2)
driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/app-xperts-page/div/div[2]/div[1]/form/div[2]/div/div[13]/button[2]").click()
Closure_Edit = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/app-xperts-page/div/div[3]/div/div[1]/div/div/table/tbody/tr[1]/td[16]/i[2]")
Closure_Edit.click()
driver.implicitly_wait(2)

#Initiate_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/div/div/div/form/div/div[1]/div/div[2]/button[2]").click()

Closure_Date = driver.find_element(By.ID,"mat-input-10")
Closure_Date.send_keys(Date_2)
Policy_Number_Button = driver.find_element(By.ID,"mat-input-11")
Policy_Number_Button.send_keys(Policy_Number)
Year_of_MFG_Button = driver.find_element(By.ID,"mat-input-12")
Year_of_MFG_Button.send_keys(Year_of_MFG)
Date_of_Reg_Button = driver.find_element(By.ID,"mat-input-23")
Date_of_Reg_Button.send_keys(Date_of_Reg)
# Policy_Start_Date_Button = driver.find_element(By.ID,"mat-input-13")
# Policy_Start_Date.send_keys(Policy_Start_Date)
Policy_End_Date_Button = driver.find_element(By.ID,"mat-input-14")
Policy_End_Date_Button.send_keys(Policy_End_Date)
IDV_Button = driver.find_element(By.ID,"mat-input-15")
IDV_Button.send_keys(IDV)
Final_Discount_Button = driver.find_element(By.ID,"mat-input-16")
Final_Discount_Button.send_keys(Final_Discount)
OD_Premium_Button = driver.find_element(By.ID,"mat-input-17")
OD_Premium_Button.send_keys(OD_Premium)
TP_Premium_Button = driver.find_element(By.ID,"mat-input-18")
TP_Premium_Button.send_keys(TP_Premium)
GST_Button = driver.find_element(By.ID,"mat-input-20")
GST_Button.send_keys(GST)
Membership_Points_Button = driver.find_element(By.ID,"mat-input-22")
Membership_Points_Button.send_keys(Membership_Points)
PaymentBy_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/div/div/div/form/div/div[2]/div[3]/div[2]/div/div[15]/ng-select/div/div/div[2]/input")
PaymentBy_Button.send_keys(PaymentBy+Keys.ENTER)
Vendor_Payment_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/div/div/div/form/div/div[2]/div[3]/div[2]/div/div[16]/ng-select/div/div/div[2]/input")
Vendor_Payment_Button.send_keys(Vendor_Payment+Keys.ENTER)
#Upload_Policy_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/div/div/div/form/div/div[2]/div[3]/div[2]/div/div[19]/fieldset/input")
# Upload_Policy_Button.send_keys("F:/Allins period/November/28-11-2021/TN GRID - NOV 2021 - 01_11_21.pdf")

# for i in Files_Data:
#     Attachment_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/div/div/div/form/div/div[1]/div/div[2]/div/button")
#     Attachment_Button.send_keys(Keys.ENTER)
#     Attachment_Button_Choose_File_Button = driver.find_element(By.XPATH,"//*[@id='eisUploadRightSideBar']/div[4]/form/div[1]/div/div[1]/input")
#     Attachment_Button_Choose_File_Button.send_keys(i)
#     Attachment_Upload_Button = driver.find_element(By.XPATH,"//*[@id='eisUploadRightSideBar']/div[4]/form/div[2]/button[1]").click()

for i in Files_Data:
    Attachment_Button = driver.find_element(By.XPATH,"/html/body/app-dashboard/div[2]/main/div/app-policyupload/div/div/div/form/div/div[1]/div/div[2]/div/button")
    Attachment_Button.send_keys(Keys.ENTER)
    Attachment_Button_Choose_File_Button = driver.find_element(By.XPATH,"//*[@id='eisUploadRightSideBar']/div[4]/form/div[1]/div/div[1]/input")
    Attachment_Button_Choose_File_Button.send_keys(i)
    driver.implicitly_wait(2)
    Attachment_Upload_Button = driver.find_element(By.XPATH,"//*[@id='eisUploadRightSideBar']/div[4]/form/div[2]/button[1]").click()


