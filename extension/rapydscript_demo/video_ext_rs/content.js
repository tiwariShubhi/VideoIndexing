alert("Hello from your Chrome extension!");
var firstHref = $("a[href^='https']").eq(0).attr("href");

console.log(firstHref);