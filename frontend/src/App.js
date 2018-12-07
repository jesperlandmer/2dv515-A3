import React, { Component } from 'react';
import { connect } from 'react-redux';

import RecommendationSelector from './components/RecommendationSelector';
import RecommendationResult from './components/RecommendationResult';
import logo from './assets/img/logo.svg';

const mapStateToProps = state => ({
  user: 'Toby'
})

class App extends Component {

  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Welcome to the Movie Recommendation System</h2>
        </div>
        <p className="App-intro">
          Welcome {this.props.user}!
          <RecommendationSelector user={this.props.user}/>
        </p>

        <RecommendationResult />
      </div>
    );
  }
}

export default connect(mapStateToProps)(App);
