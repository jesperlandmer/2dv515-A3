/* eslint-disable default-case */
import axios from 'axios';

import { SEARCH_QUERY } from '../constants/actionTypes';
import { SEARCH_QUERY_URL } from '../constants/environment';

export function search(query) {
  return {
    type: SEARCH_QUERY,
    payload: axios.get(`${SEARCH_QUERY_URL}?query=${query}`),
  };
}
