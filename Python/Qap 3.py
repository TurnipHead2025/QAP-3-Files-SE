# Description: Honest Harry's Car Lot Sales program
# Author: Sheri Evangelene
# Date(s): Nov 11, 2025- Nov 19, 2025


# Define required libraries.
import FormatValues as FV
import datetime


# Define program constants.
HST_RATE= .15
FIN_FEE= 39.99
LIC_FEE_S= 75.00
LIC_FEE_H= 165.00
TRANS_FEE= .01
TRANS_FEE_LUX= .016



# Define program functions.
def Receipt_ID():
      #Determines the receipt ID of the sale
      CustIn= CustFName [:1] + CustLName[:1]
      CustPlate= PlateNum [3:]
      CustPhone= PhoneNum [6:]
      RecID= (f"{CustIn}-{CustPlate}-{CustPhone}")

      return RecID


def First_Payment_Month():
  # Determines the first Payment
   today= datetime.datetime.now()
   PayYear= today.year
   PayMonth= today.month
   PayDay= today.day
   if PayDay > 25:
    PayMonth += 1

   FirstPay= datetime.datetime(PayYear, PayMonth, 1)

   return FirstPay


def Payment_Schedule():
 # Creates a payment schedule so the user can look at different options

 for years in range (1,5,1):   
    NumMonths = years * 12
    FinFee= FIN_FEE * years 
    TotPrice= TotSalesPrice + FinFee
    MonthlyPay= TotPrice/ NumMonths
    print(f"     {years:>4}      {NumMonths:>8}    {FV.FDollar2(FinFee):>12}{FV.FDollar2(TotPrice):>15} {FV.FDollar2(MonthlyPay):>12}")



   
    

# Main program starts here.
while True:
    
    # Gather user inputs.
  CustFName=    input("Enter the customer's first name or enter (end) to stop the program: ").title()
  if CustFName == "End":
   break
  CustLName=    input("Enter the customer's last name:                                     ").title()

  while True:
    PhoneNum =  input("Enter the customer's 10 digit phone number (9999999999):            ")
    if not len(PhoneNum) == 10:
     print("The phone number must be 10 digits.")
    else:
      break
  print()

  while True:
    PlateNum=   input("Enter your license plate number (AAA999):                           ").upper()
    if len(PlateNum) != 6:
      print(" The license's plate number must be 6 characters. ")
    elif not PlateNum [:3].isalpha():
      print("License plate must begin with three letters")
    elif not PlateNum [3:].isdigit():
      print("License plate must end with three numbers.")
    else:
      break
  
  CarMake=      input("Enter the make of your vehicle:                                     ").title()
  CarModel=     input("Enter the model of your vehicle:                                    ").title()
  CarYear=      input("Enter the year of your vehicle:                                     ").title()
  print()
  
  while True:
    try:
     SellPrice= input("Enter the selling price (under 50,000):                             ")
     SellPrice= float(SellPrice.replace(",", ""))
     if SellPrice > 50000:
      print ("Sale price must be under 50,000")
     else:
      break
    except:
      print("Enter a valid number")
      

  while True:
    try:
     TradeIn=  input("Please enter the trade in value:                                    ")
     TradeIn= float(TradeIn.replace(",","")) 
     if TradeIn > SellPrice:
      print("The trade in cannot exceed the sale price")
     else:
      break
    except:
      print("Enter a valid number")
  print()    

  SalesName=   input("Enter the salesperson's name:                                       ").title()



   # Perform required calculations.
 
  
  if SellPrice <= 15000:
    LicFee= LIC_FEE_S
  elif SellPrice > 15000:
    LicFee= LIC_FEE_H

  TransFee= SellPrice * TRANS_FEE
  if SellPrice > 20000:
    TransFee = (SellPrice * TRANS_FEE_LUX) + TransFee

  PriceAfTrade= SellPrice -TradeIn

  SubTot= PriceAfTrade + LicFee + TransFee
  HST= HST_RATE * SubTot
  TotSalesPrice= SubTot + HST

  PhoneNumDSP=(f"({PhoneNum [:3]}) {PhoneNum[3:6]}-{PhoneNum[6:]} ")    

  CustInDis= (f"{CustFName[:1]}. {CustLName}")  
 
  InvDate= datetime.datetime.now()



    # Display results
  print("-------------------------------------------------------------------------")
  print()
  print()  
  print(f"Honest Harry Car Sales                       Invoice Date:   {FV.FDateMon(InvDate): >12}")
  print(f"Used Car Sale and Receipt                    Receipt No:    {Receipt_ID():>13}")
  print()
  print(f"                                       Sale price:            {FV.FDollar2(SellPrice):>11}")
  print(f"Sold to:                               Trade Allowance:       {FV.FDollar2(TradeIn):>11}")
  print("                                       ----------------------------------") 
  print(f"     {CustInDis:<23}           Price after Trade:     {FV.FDollar2(PriceAfTrade):>11}")
  print(f"     {PhoneNumDSP:}                   License Fee:           {FV.FDollar2(LicFee):>11}")
  print(f"                                       Transfer Fee:          {FV.FDollar2(TransFee):>11}")
  print("                                       ----------------------------------") 
  print(f"Car Details:                           Subtotal:              {FV.FDollar2(SubTot):>11}")
  print(f"                                       HST:                   {FV.FDollar2(HST):>11} ")
  print(f"     {CarYear:<4} {CarMake:<13} {CarModel:<10}     ----------------------------------") 
  print(f"                                       Total Sales Price:     {FV.FDollar2(TotSalesPrice):>9}")
  print()
  print("-------------------------------------------------------------------------")
  print()
  print("                                Financing      Total        Monthly  ")                              
  print(f"     # Years     # Payments        Fee         Price        Payment ")
  print("     --------------------------------------------------------------")
  Payment_Schedule()
  print("     --------------------------------------------------------------")
  print(f"     First Payment Date:   {FV.FDateD(First_Payment_Month())}")
  print("-------------------------------------------------------------------------")
  print("                    Best used cars at the best prices, honestly!")
  print()
        



  

    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.