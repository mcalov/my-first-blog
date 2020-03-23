    var xhttp = new XMLHttpRequest();
    var theData2=[];
    var theData = [
			{ y: 450 },
			{ y: 414},
			{ y: 520, indexLabel: "highest",markerColor: "red", markerType: "triangle" },
			{ y: 460 },
			{ y: 450 },
			{ y: 500 },
			{ y: 480 },
			{ y: 480 },
			{ y: 410 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross" },
			{ y: 500 },
			{ y: 480 },
			{ y: 510 }
		];
    function getData(){
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        //document.getElementById("jsonContainer").innerHTML = this.responseText;
        puff = JSON.parse(this.responseText);
        console.log(puff);
        for(i = 0; i<puff.length;i++){
                theData.push({y:puff[i].BWSField.Einwohner});
        }
        createChart();
                jQuery.getJSON("http://127.0.0.1:8000/data" , function(data){
                    console.log(data);
                    var i = data.length;
                    var jahrBegin = 2006;
                    var jahrEnd = 2011;
                    for(idx=0;idx<i;idx++){
                        if(data[idx].Jahr>=jahrBegin && data[idx].Jahr <=jahrEnd){
                            if(data[idx].Landkreis=="Deutschland" || data[idx].Landkreis=="Brandenburg"){
                                    theData2.push({y:data[idx].BWSField.Einwohner});
                                }
                        }
                    }
                    createChart2();
                });


      }
    }
    xhttp.open("GET", "http://127.0.0.1:8000/data", true);
    xhttp.send();


    createChart = function(){
    var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Simple Line Chart"
	},
	axisY:{
		includeZero: false
	},
	data: [{
		type: "line",
		dataPoints: theData
	}]
    });
    chart.render();
    }

    createChart2 = function(){
    var chart = new CanvasJS.Chart("chartContainer2", {
	animationEnabled: true,
	theme: "light2",
	title:{
		text: "Simple Line Chart"
	},
	axisY:{
		includeZero: true
	},
	data: [{
		type: "line",
		dataPoints: theData2
	}]
    });
    chart.render();
    }
    }
var el = document.getElementById("butn1");
el.addEventListener("click", getData);
