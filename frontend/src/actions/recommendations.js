/* eslint-disable default-case */
import axios from 'axios';

import { USER_BASED_ROOT, ITEM_BASED_ROOT } from '../constants/environment';

export function fetchUserBasedRec(user, type) {
  switch (type) {
    case 'USER_BASED_PEARSON':
      return {
        type,
        payload: axios.get(`${USER_BASED_ROOT}/pearson?_user=${user}`),
      };
    default:
    case 'USER_BASED_EUCLIDEAN':
      return {
        type,
        payload: axios.get(`${USER_BASED_ROOT}/euclidean?_user=${user}`),
      };
  }
}

export function fetchItemBasedRec(user, type) {
  return {
    type: 'ITEM_BASED_EUCLIDEAN',
    payload: axios.get(`${ITEM_BASED_ROOT}/euclidean?_user=${user}`),
  };
}
