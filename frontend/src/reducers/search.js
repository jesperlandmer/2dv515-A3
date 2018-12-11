const initialState = {
  fetching: false,
  fetched: false,
  result: [],
  error: null
}

function compare(a, b) {
  const scoreA = a.score;
  const scoreB = b.score;

  let comp = 0;
  if (scoreA > scoreB) {
    comp = 1;
  } else if (scoreA < scoreB) {
    comp = -1;
  }

  return comp * -1;
}

export default (state = initialState, action) => {
  switch(action.type) {
    case "SEARCH_QUERY_PENDING":
      return {...state, fetching: true }
    case "SEARCH_QUERY_REJECTED":
      return {...state, fetching: false, fetched: false, error: action.payload}
    case "SEARCH_QUERY_FULFILLED":
      const { data } = action.payload;
      return {...state, fetching: false, fetched: true, error: null, result: data.sort(compare).slice(0,5)}
    default:
      return state;
  }
}
