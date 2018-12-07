// use 'proxy' field in package.json to send requests, avoiding CORS issues
// eslint-disable-next-line import/prefer-default-export
export const USER_BASED_ROOT = '/api/ub';
export const ITEM_BASED_ROOT = '/api/ib';

export const recMethods = {
    'user-based': ['euclidean', 'pearson'],
    'item-based': ['euclidean'],
}