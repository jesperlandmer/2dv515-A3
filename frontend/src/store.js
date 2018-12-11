import { applyMiddleware, createStore } from 'redux';
import { createLogger } from 'redux-logger';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';
import promise from 'redux-promise-middleware';

import reducer from './reducer';

const configureStore = () => {
  const store = createStore(
    reducer,
    composeWithDevTools(
      applyMiddleware(promise(), thunk, createLogger()),
    )
  );

  if (process.env.NODE_ENV !== 'production') {
    if (module.hot) {
      module.hot.accept('./reducer', () => {
        store.replaceReducer(reducer);
      });
    }
  }

  return store;
};

export default configureStore;
