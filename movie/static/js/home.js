function odliczaj() //ZEGAR i DATA
{
  today = new Date();
  let day = today.getDate();
  let month = today.getMonth()+1;
  let year = today.getFullYear();
  let hour = today.getHours();

  if(hour<10) hour = "0"+hour;
  let minute = today.getMinutes();
  if(minute<10) minute = "0"+minute;
  let second = today.getSeconds();
  if(second<10) second = "0"+second;
  document.getElementById("clock").innerHTML =
  day+"/"+month+"/"+year+" | "+hour+":"+minute+":"+second;
  setTimeout("odliczaj()",1000);
}



const tabItems = document.querySelectorAll('.tab-item');
const tabContentItems = document.querySelectorAll('.tab-content-item');

// Select tab content item
function selectItem(e) {
	// Remove all show and border classes
	removeBorder();
	removeShow();
	// Add border to current tab item
	this.classList.add('tab-border');
	// Grab content item from DOM
	const tabContentItem = document.querySelector(`#${this.id}-content`);
	// Add show class
	tabContentItem.classList.add('show');
}

// Remove bottom borders from all tab items
function removeBorder() {
	tabItems.forEach(item => {
		item.classList.remove('tab-border');
	});
}

// Remove show class from all content items
function removeShow() {
	tabContentItems.forEach(item => {
		item.classList.remove('show');
	});
}

// Listen for tab item click
tabItems.forEach(item => {
	item.addEventListener('click', selectItem);
});






