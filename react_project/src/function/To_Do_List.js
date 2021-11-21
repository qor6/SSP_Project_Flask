document.getElementById("btnAdd").addEventListener("click",addList);
// html에서 id가 btnAdd인 요소를 찾고 클릭 시 동작할 addList 함수 연결

function addList() {
    var contents = document.querySelector(".text-basic");
    // 입력창에 접근

    if(!contents.value) // 입력창에 값이 없으면
    {
        alert("데이터를 입력해주세요."); // 경고창 출력

        contents.focus();
        // 입력창에 포커스 (활성화)

        return false;
        // 함수 종료
    }

    // ***** 데이터 추가 *****
    var tr = document.createElement("tr"); // 추가할 테이블 <tr> 생성
    var input = document.createElement("input"); // 테이블 <tr> 안에 들어갈 체크박스의 <input> 생성

    // 여기서 생성된 <tr> 안에는
    // <td>체크박스</td>
    // <td>텍스트<td>
    // 이렇게 두 가지의 요소가 들어가야 함

    // 체크박스 만들기
    input.setAttribute("type","checkbox"); // <input type="checkbox">
    input.setAttribute("class","btn-chk"); // <input type="checkbox" class="btn-chk">

    var td01=document.createElement("td"); // 첫 번째 <td> 생성 (체크박스를 담음)
    td01.appendChild(input); // 첫 번째 <td> 안에 <input> 추가

    var td02 = document.createElement("td"); // 두 번째 <td> 생성 (텍스트를 담음)
    td02.innerHTML = contents.value; // 두 번째 <td> 안에 입력창의 텍스트를 저장

    tr.appendChild(td01);
    tr.appendChild(td02); // 생성된 <tr> 안에 체크박스 td와 텍스트 td를 넣음

    document.getElementById("listBody").appendChild(tr); // tbody의 #listBody에 접근하여 tr을 자식요소로 추가

    contents.value=""; // 입력창의 내용이 추가되었으므로 입력창 지우기

    contents.focus(); // 입력창 포커스 (활성화)

    // 지우기 버튼
    const button = document.createElement("button");
    button.innerText="×";
    button.addEventListener("click", deleteToDo);
    tr.appendChild(button);

}

// 삭제 함수
function deleteToDo(value) {
  const tr=value.target.parentElement;
  tr.remove();
}
