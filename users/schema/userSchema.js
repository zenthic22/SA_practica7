const { gql } = require('apollo-server-express');
const userResolvers = require('../resolvers/userResolvers');

const typeDefs = gql`
  type User {
    id: Int
    name: String
    email: String
  }

  type Query {
    allUsers: [User]
    userById(id: Int!): User
  }

  type Mutation {
    createUser(name: String!, email: String!): User
    updateUser(id: Int!, name: String!, email: String!): User
    deleteUser(id: Int!): String
  }
`;

module.exports = { typeDefs, resolvers: userResolvers };