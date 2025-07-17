clear
use "dataRaw321 (State).dta"

**WI*********************************
	*switch lines 4 & 6 with whichever states
drop if state!="WI"
tsset quarter, quarterly

varsoc output price employ wage numfirm
	*predominantly records 4 lags

vecrank output price employ wage numfirm, lags(4)
*trend(constant)
	*results in Rank = 2 (whether or not I use the options I've commented out..?)

******USE A VEC MODEL******
	
*VEC MODEL
vec output price employ wage numfirm, rank(2) lags(4) noetable

*Forecast 5 years into the future*
fcast compute f_, step(20)

label variable f_employ "Forecast"
label variable f_wage "Forecast"
label variable f_numfirm "Forecast"
label variable f_price "Forecast"
label variable f_output "Forecast"

*If you want to see the error bounds:
*fcast graph f_employ f_wage f_numfirm f_price f_output, byopts(iscale(*.8))

tostring quarter, gen(Time)
replace time = "2019q1" if Time == "236"
replace time = "2019q2" if Time == "237"
replace time = "2019q3" if Time == "238"
replace time = "2019q4" if Time == "239"
replace time = "2020q1" if Time == "240"
replace time = "2020q2" if Time == "241"
replace time = "2020q3" if Time == "242"
replace time = "2020q4" if Time == "243"
replace time = "2021q1" if Time == "244"
replace time = "2021q2" if Time == "245"
replace time = "2021q3" if Time == "246"
replace time = "2021q4" if Time == "247"
replace time = "2022q1" if Time == "248"
replace time = "2022q2" if Time == "249"
replace time = "2022q3" if Time == "250"
replace time = "2022q4" if Time == "251"
replace time = "2023q1" if Time == "252"
replace time = "2023q2" if Time == "253"
replace time = "2023q3" if Time == "254"
replace time = "2023q4" if Time == "255"

******ROBUSTNESS CHECK******
vec output price employ wage numfirm if quarter <= tq(2016q1), rank(1) lags(4) noetable

*Forecast 5 years into the future*
fcast compute rcf_, step(12)

label variable rcf_employ "Robustness Check"
label variable rcf_wage "Robustness Check"
label variable rcf_numfirm "Robustness Check"
label variable rcf_price "Robustness Check"
label variable rcf_output "Robustness Check"

replace state="WI" if state==""
keep time quarter state employ wage numfirm price output f_employ f_wage ///
f_numfirm f_price f_output rcf_employ rcf_wage rcf_numfirm rcf_price rcf_output
******************
*line rcf_employ employ quarter

save WI
