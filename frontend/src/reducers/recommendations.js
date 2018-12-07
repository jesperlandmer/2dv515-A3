const initialState = {
  fetching: false,
  fetched: false,
  recommendations: [],
  error: null
}

export default (state = initialState, action) => {
  switch(action.type) {
    case "USER_BASED_EUCLIDEAN_PENDING":
      return {fetching: true}
    case "USER_BASED_EUCLIDEAN_REJECTED":
      return {...state, fetching: false, fetched: false, error: action.payload}
    case "USER_BASED_EUCLIDEAN_FULFILLED":
      return {...state, fetching: false, fetched: true, recommendations: action.payload.data}
    case "USER_BASED_PEARSON_PENDING":
      return {fetching: true}
    case "USER_BASED_PEARSON_REJECTED":
      return {...state, fetching: false, fetched: false, error: action.payload}
    case "USER_BASED_PEARSON_FULFILLED":
      return {...state, fetching: false, fetched: true, recommendations: action.payload.data}
    case "ITEM_BASED_EUCLIDEAN_PENDING":
      return {fetching: true}
    case "ITEM_BASED_EUCLIDEAN_REJECTED":
      return {...state, fetching: false, fetched: false, error: action.payload}
    case "ITEM_BASED_EUCLIDEAN_FULFILLED":
      return {...state, fetching: false, fetched: true, recommendations: action.payload.data}
    default:
      return state;
  }
}
