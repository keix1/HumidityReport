# On script editor spreadsheet

function doGet(e) {
	var humidity = e.parameter.humidity;
	var temperature = e.parameter.temperature;
	var sheet = SpreadsheetApp.getActiveSheet();
	sheet.appendRow([new Date(), temperature, humidity]);
}
