import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Table } from 'react-bootstrap';

const mapStateToProps = state => ({
  searchResult: state.search.result,
})

class SearchResult extends Component {

  render() {
    const { searchResult } = this.props;

    return searchResult.length > 0 ? (
    <Table striped bordered condensed hover>
    <thead>
        <tr>
        <th>#</th>
        <th>Name</th>
        <th>WR</th>
        </tr>
    </thead>
    <tbody>
        {searchResult.map((score, key) => 
                <tr>
                    <td>{key + 1}</td>
                    <td>{score.link}</td>
                    <td>{score.score}</td>
                </tr>
            )}
    </tbody>
    </Table>
    ) : <div></div>;
  }
}

export default connect(mapStateToProps)(SearchResult);
