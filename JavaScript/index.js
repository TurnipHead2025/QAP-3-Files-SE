// Desc: Lawncare service receipt
// Author: Sheri Evangelene
// Dates: Nov 14, 2025 - Nov 20, 2025


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.
const BORDERS_SIZE = .04;
const BORDERS_RATE= .28;
const MOWING_SIZE= .95;
const MOWING_RATE= .04;
const FERT_RATE= .03;
const HST_RATE= .15;
const ENVIRO_TAX_RATE= .014;



// Start main program here.

// User Inputs
let custName= prompt("Enter your name: ");
let stAdd= prompt("Enter your street address: ");
let city= prompt("Enter your city: ");
let phoneNum= prompt("Enter your phone number: ");
let sqFt= parseInt(prompt("Enter your total square feet: "));


// Calculations
let borders= (BORDERS_SIZE * sqFt) * BORDERS_RATE;
let lawnMow= (MOWING_SIZE* sqFt) * MOWING_RATE;
let fert= FERT_RATE * sqFt;

let totChr= borders + lawnMow + fert
let salesTax= totChr * HST_RATE
let enviroTax = totChr * ENVIRO_TAX_RATE

let invTot= totChr + salesTax + enviroTax

// Output
document.writeln("<table>");

document.writeln("<tr>");
document.writeln("<td colspan='2' class='orgtext'><br>Mo's Lawncare Services-Customer Invoice<br>\xa0</td>");
document.writeln("</tr>");


document.writeln("<tr>");
document.writeln("<td colspan='2'><br>Customer details:<br><br>");
document.writeln("\xa0\xa0\xa0\xa0\xa0\xa0\xa0 " + custName + "<br>");
document.writeln("\xa0\xa0\xa0\xa0\xa0\xa0\xa0 " + stAdd + "<br>");
document.writeln("\xa0\xa0\xa0\xa0\xa0\xa0\xa0 " + city + "\xa0\xa0" + phoneNum + "<br><br>\xa0");
document.writeln("Property size (in sq ft):\xa0" + sqFt + "<br>\xa0");
document.writeln("</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Border cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(borders) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Mowing cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(lawnMow) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Fertilizer cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(fert) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br></td>");
document.writeln("<td></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Total charges:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(totChr) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br></td>");
document.writeln("<td></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Sales tax (HST):</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(salesTax) + "</td>");
document.writeln("</tr>");


document.writeln("<tr>");
document.writeln("<td>Enviromental tax:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(enviroTax) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br></td>");
document.writeln("<td></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Invoice total:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(invTot) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2' class='orgtext'><br>Turning Lawns into Landscapes<br>\xa0</td>");
document.writeln("</tr>");

document.writeln("</table>");

