import PyPDF2
import json

keys = [
    "Name",
    "PAN",
    "Date of Birth (DD/MM/YYYY)",
    "Mobile no",
    "Email Address",
    "Aadhaar Number (Please enter the Aadhaar Number if alloted)",
    "Address",
    "Flat / Door / Block No",
    "Name of Premises / Building / Village",
    "Road/ Street",
    "Area/ Locality",
    "Town/ City/ District",
    "State",
    "PIN Code",
    "Filing Status",
    "Employer category (If in employment)",
    "Section",
    "Filing Type",
    "Notice Number",
    "If filed in response to notice u/s 139(9)/142(1)/148/153A/153C, enter the date of such notice",
    "Are you governed by Portuguese Civil Code as per section 5A ?",
    "If Yes,Fill PAN of the Spouse",
    "Part B Gross Total Income",
    "(i) Salary (excluding all allowances, perquisites and profit in lieu of salary)",
    "(ii) Allowances not exempt",
    "(iii) Value of perquisites",
    "(iv) Profits in lieu of salary",
    "(v) Deduction u/s 16",
    "(vi) Income chargeable under the Head 'Salaries' (i+ii+iii+iv-v)",
    "Type of House Property",
    "(i) Gross rent received/ receivable/ letable value",
    "(ii) Tax paid to local authorities",
    "(iii) Annual Value (i - ii)",
    "(iv) 30% of Annual Value",
    "(v) Interest payable on borrowed capital",
    "(vi) Income chargeable under the head 'House Property' (iii - iv - v) ",
    "B3",
    "Income from Other Sources",
    "B4",
    " Gross Total Income (B1+B2+B3)(If loss, put the figure in negative)",
    "PART C - DEDUCTIONS AND TAXABLE TOTAL INCOME (Refer instructions for Deduction limit as per Income-tax Act)",
    "80C - Life insurance premia, deferred annuity, contributions to provident",
    "fund, subscription to certain equity shares or debentures, etc.",																	
    "80CCC - Payment in respect Pension Fund",																	
    "80CCD(1) - Contribution to pension scheme of Central Government",																	
    "80CCD(1B) - Contribution to pension scheme of Central Government																	
    "80CCD(2) - Contribution to pension scheme of Central Government by
    "employer																	
    "80CCG - Investment made under an equity savings scheme																	
    "80D																	
    "(A) Health Insurance Premium -",																
    "(B) Medical expenditure - Self and family (including senior and very senior",
    "citizen)",
    "(C) Preventive health check-up -",
    "80DD - Maintenance including medical treatment of a dependent who is a",
    "person with disability -",
    "80DDB - Medical treatment of specified disease -",
    "80E - Interest on loan taken for higher education",
    "80EE - Interest on loan taken for residential house property",
    "80G - Donations to certain funds, charitable institutions, etc",
    "80GG - Rent paid",
    "80GGA - Certain donations for scientific research or rural development",
    "80GGC - Donation to Political party",
    "80RRB - Royalty on patents",
    "80QQB - Royalty income of authors of certain books.",
    "80TTA - Income from Interest on saving bank Accounts",
    "80U- In case of a person with disability.-",
    "Total Deductions",
    "Note:Total deductions under chapter VI A cannot exceed GTI.",
    "Total Income (B4-C1)",
    "Part D - Computation of Tax Payable",
    "Tax Payable on Total Income(C2)",
    "Rebate u/s 87A",
    "Tax after Rebate (D1-D2)",
    "Cess, on D3",
    "Total Tax and Cess",
    "Relief u/s 89(1)",
    "Balance Tax After Relief (D5-D6)",
    "Interest u/s 234A",
    "Interest u/s 234B",
    "Interest u/s 234C",
    "Fee u/s 234F",
    "Total Interest and Fee Payable ( D7 + D8 + D9 + D10)",
    "Total Tax, Fee and Interest ( D5 + D7 + D8 + D9 + D10 - D6 )",
    "Total Advance Tax Paid",
    "Total Self Assessment Tax Paid",
    "Total TDS Claimed",
    "Total TCS Collected",
    "Total Taxes Paid(D12[(i) + (ii) + (iii) + (iv)])",
    "Amount payable (D11 - D12)(if D11 > D12)",
    "Refund(D12 - D11)(if D12 > D11)",
    "Exempt income (For reporting Purposes)",
    "Sec.10(38) (Exempted Long term Capital Gains)",
    "Sec.10(34) (Exempted Dividend Income)",
    "Agriculture Income (<= Rs.5000)",
    "Others",
    "Nature of Income",
    "Description ( If 'Any Other' selected)",

                                                                        


]

import PyPDF2
import json

keys = [
    "Name",
    "PAN",
    "Date of Birth (DD/MM/YYYY)",
    "Mobile no",
    "Email Address",
    "Aadhaar Number (Please enter the Aadhaar Number if alloted)",
    "Address",
    "Flat / Door / Block No",
    "Name of Premises / Building / Village",
    "Road/ Street",
    "Area/ Locality",
    "Town/ City/ District",
    "State",
    "PIN Code",
    "Filing Status",
    "Employer category (If in employment)",
    "Section",
    "Filing Type",
    "Notice Number",
    "If filed in response to notice u/s 139(9)/142(1)/148/153A/153C, enter the date of such notice",
    "Are you governed by Portuguese Civil Code as per section 5A ?",
    "If Yes,Fill PAN of the Spouse",
    "Part B Gross Total Income",
    "(i) Salary (excluding all allowances, perquisites and profit in lieu of salary)",
    "(ii) Allowances not exempt",
    "(iii) Value of perquisites",
    "(iv) Profits in lieu of salary",
    "(v) Deduction u/s 16",
    "(vi) Income chargeable under the Head 'Salaries' (i+ii+iii+iv-v)",
    "Type of House Property",
    "(i) Gross rent received/ receivable/ letable value",
    "(ii) Tax paid to local authorities",
    "(iii) Annual Value (i - ii)",
    "(iv) 30% of Annual Value",
    "(v) Interest payable on borrowed capital",
    "(vi) Income chargeable under the head 'House Property' (iii - iv - v) ",
    "B3",
    "Income from Other Sources",
    "B4",
    " Gross Total Income (B1+B2+B3)(If loss, put the figure in negative)",
    "PART C - DEDUCTIONS AND TAXABLE TOTAL INCOME (Refer instructions for Deduction limit as per Income-tax Act)",
    "80C - Life insurance premia, deferred annuity, contributions to provident",
    "fund, subscription to certain equity shares or debentures, etc.",																	
    "80CCC - Payment in respect Pension Fund",																	
    "80CCD(1) - Contribution to pension scheme of Central Government",																	
    "80CCD(1B) - Contribution to pension scheme of Central Government																	
    "80CCD(2) - Contribution to pension scheme of Central Government by
    "employer																	
    "80CCG - Investment made under an equity savings scheme																	
    "80D																	
    "(A) Health Insurance Premium -",																
    "(B) Medical expenditure - Self and family (including senior and very senior",
    "citizen)",
    "(C) Preventive health check-up -",
    "80DD - Maintenance including medical treatment of a dependent who is a",
    "person with disability -",
    "80DDB - Medical treatment of specified disease -",
    "80E - Interest on loan taken for higher education",
    "80EE - Interest on loan taken for residential house property",
    "80G - Donations to certain funds, charitable institutions, etc",
    "80GG - Rent paid",
    "80GGA - Certain donations for scientific research or rural development",
    "80GGC - Donation to Political party",
    "80RRB - Royalty on patents",
    "80QQB - Royalty income of authors of certain books.",
    "80TTA - Income from Interest on saving bank Accounts",
    "80U- In case of a person with disability.-",
    "Total Deductions",
    "Note:Total deductions under chapter VI A cannot exceed GTI.",
    "Total Income (B4-C1)",
    "Part D - Computation of Tax Payable",
    "Tax Payable on Total Income(C2)",
    "Rebate u/s 87A",
    "Tax after Rebate (D1-D2)",
    "Cess, on D3",
    "Total Tax and Cess",
    "Relief u/s 89(1)",
    "Balance Tax After Relief (D5-D6)",
    "Interest u/s 234A",
    "Interest u/s 234B",
    "Interest u/s 234C",
    "Fee u/s 234F",
    "Total Interest and Fee Payable ( D7 + D8 + D9 + D10)",
    "Total Tax, Fee and Interest ( D5 + D7 + D8 + D9 + D10 - D6 )",
    "Total Advance Tax Paid",
    "Total Self Assessment Tax Paid",
    "Total TDS Claimed",
    "Total TCS Collected",
    "Total Taxes Paid(D12[(i) + (ii) + (iii) + (iv)])",
    "Amount payable (D11 - D12)(if D11 > D12)",
    "Refund(D12 - D11)(if D12 > D11)",
    "Exempt income (For reporting Purposes)",
    "Sec.10(38) (Exempted Long term Capital Gains)",
    "Sec.10(34) (Exempted Dividend Income)",
    "Agriculture Income (<= Rs.5000)",
    "Others",
    "Nature of Income",
    "Description ( If 'Any Other' selected)",

                                                                    
]

file = open('file.pdf', 'rb')

fileReader = PyPDF2.PdfFileReader(file)

def getPage(pageNo, keys):
	pageObj = fileReader.getPage(pageNo)

	text = pageObj.extractText()

	array = text.split("\n")

	ack_no = array[0].split(" ")[-1]

	data = {"Acknowledgement Number": ack_no}

	for i in range(len(keys)):
	    if keys[i] in array:
	        ind = array.index(keys[i])
	        if(ind < len(array)-1 and i < len(keys)-1 and array[ind + 1] == keys[i + 1]):
	            data[keys[i]] = "null"
	        else:
	            data[keys[i]] = array[ind + 1]
    finalJson0 = json.dumps(data, indent=2)

    return finalJson0


page1 = getPage(0, keys);
page2 = getPage(1, keys);
page3 = getPage(2, keys);

print(page1)
print(page2)
print(page3)