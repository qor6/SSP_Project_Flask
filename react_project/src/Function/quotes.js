// 랜덤으로 명언나옴
const quotes = [
  {
    quote: "우리의 인생은 우리가 노력한 만큼 가치가 있다.",
    author: " -모리악-",
  },
  {
    quote: "세상의 중요한 일의 대부분은 희망이 없어 보였을때 끊임없이 도전한 사람들에 의해 이루어졌다.",
    author: " -데일카네-",
  },
  {
    quote: "우리의 가장 큰 영광은 결코 실패하지않음이 아니라 떨어질때마다 일어서는 것이다.",
    author: " -공자-",
  },
  {
    quote: "편견은 내가 다른 사람을 사랑하지 못하게 하고 오만은 다른사람이 나를 사랑하지 못하게 한다.",
    author: " -오만과 편견,2005-",
  },
  {
    quote: "겨울이 오면 봄이 멀지 않으리",
    author: " -퍼시 셸리-",
  },
  {
    quote: "꿈을 향해 달리는 순간 그것은 더 이상 꿈이 아니죠.",
    author: " -피터팬,1957-",
  },
  {
    quote: "나는 낙심하지 않는다 실패한 모든 시도들은 다음 시도를 위한 또 다른 발걸음이기 때문이다.",
    author: " -토머스 에디슨-",
  },
  {
    quote: "작은 변화를 만들어 낼 때 진짜 삶이 시작된다.",
    author: "-레프 톨스토이-",
  },
  {
    quote: "맹인으로 태어나는 것보다 더 비극적인 일은 앞은 볼 수 있으나 비전이 없는 것이다.",
    author: " -헬렌 켈러-",
  },
  {
    quote: "자신의 인생이 끝날까 두려워하지 마라 자신의 인생이 아직 시작조차 하지 않았을 수 있다는 사실을 두려워하라.",
    author: " -그레이스 한센-",
  },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");
const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;
