const cards = document.querySelectorAll('.Stock__Item');
const mediaQuery = window.matchMedia('(max-width: 980px)');

function handleMouseEnter() {
  this.style.transform = 'scale(1.2)';
  this.style.transition = '0.25s';
  this.style.cursor = 'pointer';
}

function handleMouseLeave() {
  this.style.transform = 'scale(1)';
}

function checkScreenSize() {
  if (mediaQuery.matches) {
    cards.forEach(card => {
      card.removeEventListener('mouseenter', handleMouseEnter);
      card.removeEventListener('mouseleave', handleMouseLeave);
    });
  } else {
    cards.forEach(card => {
      card.addEventListener('mouseenter', handleMouseEnter);
      card.addEventListener('mouseleave', handleMouseLeave);
    });
  }
}

// เรียกใช้ฟังก์ชันเพื่อตรวจสอบขนาดหน้าจอเมื่อโหลดหน้าเว็บ
checkScreenSize();

// เพิ่ม event listener เพื่อตรวจสอบการเปลี่ยนแปลงขนาดหน้าจอ
window.addEventListener('resize', checkScreenSize);




document.addEventListener('DOMContentLoaded', function() {
  var stockItems = document.querySelectorAll('.Stock__Item');

  stockItems.forEach(function(item) {
      item.addEventListener('click', function() {
          var itemId = item.getAttribute('data-id');
          window.location.href = 'Stock_History/' + itemId;
      });
  });
});

const wrapper = document.querySelector('.wapper'),
selectbtn = wrapper.querySelector('.select-btn'),
options = wrapper.querySelector('.option'),
inputInp = wrapper.querySelector('input');

let stocks = [];

function fetchDataAndInitialize() {
  fetch('/Stock_info/Symbol_API')
      .then(response => response.json())
      .then(data => {
          stocks = data.filter(stock => stock.TypeSector === 4 || stock.TypeSector === 1);
          stocks.sort((a, b) => a.Symbolname.localeCompare(b.Symbolname));
          addStocks(); 
      })
      .catch(error => console.error('Error: ', error));
}
function addStocks() {
options.innerHTML = "";
stocks.forEach(stock => {
    let li = `<li value="${stock.id}" onclick="updateStock(this)">${stock.Symbolname}</li>`;
    options.insertAdjacentHTML('beforeend', li);
});
}

function updateStock(selected) {
  const stockId = selected.getAttribute('value');
  const stockName = selected.innerHTML;

  inputInp.value = stockName;
  inputInp.setAttribute('value', stockId);
  wrapper.classList.remove('active');
  selectbtn.firstElementChild.innerHTML = stockName;
  }

inputInp.addEventListener('keyup', () => {
  let arr = [];
  let searchVal = inputInp.value.toLowerCase();

  arr = stocks.filter(data => {
      return data.Symbolname.toLowerCase().includes(searchVal);
  }).map(data => `<li value="${data.id}" onclick="updateStock(this)">${data.Symbolname}</li>`).join("");
  options.innerHTML = arr ? arr : `<p>Oops! not found</p>`;
  });

  selectbtn.addEventListener('click', () => {
  wrapper.classList.toggle('active');
});

fetchDataAndInitialize();



const AVG = document.querySelector('#AVG');
const Amounts = document.querySelector("#Amounts");
const Values = document.querySelector('#Values');
const BtnSaved = document.querySelector('#BtnSaved');
const date = document.querySelector('#date');

function calculate() {
  const avgValue = parseFloat(AVG.value);
  const amountsValue = parseInt(Amounts.value);
  const dateValue = Date.parse(date.value);
  
  if (!isNaN(avgValue) && !isNaN(amountsValue) && !isNaN(dateValue)) {
    Values.innerHTML = `Purchase Amount : <span style="color:Green;">$${(avgValue * amountsValue).toFixed(2)}</span>`;
    BtnSaved.disabled = false;
  } else {
    Values.innerHTML = "";
    BtnSaved.disabled = true;
  }
}

function handleInput(event) {
  const input = event.target.value;
  const regex = /^[0-9.]*$/; // ตรวจสอบว่ามีเฉพาะตัวเลขและจุดทศนิยมเท่านั้น
  if (!regex.test(input)) {
    event.target.value = input.replace(/[^0-9.]/g, ''); // ลบอักขระที่ไม่ใช่ตัวเลขหรือจุดทศนิยม
  }
}

AVG.addEventListener('input', handleInput);
Amounts.addEventListener('input', handleInput);
AVG.addEventListener('input', calculate);
Amounts.addEventListener('input', calculate);
date.addEventListener('input', calculate);



const StartPopupNewHistory = document.querySelector('#StartPopupNewHistory');
const EndPopupNewHistory = document.querySelector('#EndPopupNewHistory');
const PopUP = document.querySelector("#Pop-up");


StartPopupNewHistory.addEventListener('click', function () {
  PopUP.classList.remove('hidden');
});

EndPopupNewHistory.addEventListener('click', function () {
  PopUP.classList.add('hidden')
});