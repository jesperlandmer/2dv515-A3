import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Table } from 'react-bootstrap';

const mapStateToProps = state => ({
  recommendations: state.recommendations.recommendations,
})

class RecommendationResult extends Component {

  render() {
    return this.props.recommendations.length > 0 ? (
    <Table striped bordered condensed hover>
    <thead>
        <tr>
        <th>#</th>
        <th>Name</th>
        <th>WR</th>
        </tr>
    </thead>
    <tbody>
        {this.props.recommendations.map((movie, key) => 
                <tr>
                    <td>{key + 1}</td>
                    <td>{movie.name}</td>
                    <td>{movie.weightedScore}</td>
                </tr>
            )}
    </tbody>
    </Table>
    ) : <div></div>;
  }
}

export default connect(mapStateToProps)(RecommendationResult);
