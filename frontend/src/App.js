import React, { Component } from 'react';
import { connect } from 'react-redux';

import SearchForm from './components/SearchForm';
import SearchResult from './components/SearchResult';
import logo from './assets/img/logo.svg';

class App extends Component {

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to the Search Engine</h2>
        </div>
        <p className="App-intro">
          Search for something!
          <SearchForm />
        </p>

        <SearchResult />
      </div>
    );
  }
}

export default connect()(App);
