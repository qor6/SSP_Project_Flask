function count(type)  {
  // 결과를 표시할 element
  const resultElement = document.getElementById('result');

  // 현재 화면에 표시된 값
  let number = resultElement.innerText;

  // 더하기
    number = parseInt(number) + 1;

  // 결과 출력
  resultElement.innerText = number;
}
