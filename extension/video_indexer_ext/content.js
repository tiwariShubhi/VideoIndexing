alert("Hello from your Chrome extension!");
//var firstHref = $("a[href^='https']").eq(0).attr("href");

//console.log(firstHref);

var video_url = window.location.href;
var servlet_url = "http://localhost:8080/VideoIndexing/Run_Indexer"
//var params = json2urlParams(data);
jQuery.ajax({
        type : "POST", 
        url : servlet_url, 
        data : {video_url : video_url}, 
        success : function (data, textStatus, XMLHttpRequest) {
            console.log("Data Saved: " + msg);
        }
    });