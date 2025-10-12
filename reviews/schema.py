import graphene
from models.review import Review

#Tipo review para GraphQL
class ReviewType(graphene.ObjectType):
    id = graphene.Int()
    user_id = graphene.Int()
    movie_id = graphene.Int()
    comment = graphene.String()
    rating = graphene.Int()

# Query
class Query(graphene.ObjectType):
    all_reviews = graphene.List(ReviewType)
    review_by_id = graphene.Field(ReviewType, id=graphene.Int(required=True))

    def resolve_all_reviews(self, info):
        reviews, err = Review.get_all()
        if err:
            raise Exception(err)
        return [ReviewType(**r) for r in reviews]

    def resolve_review_by_id(self, info, id):
        review, err = Review.get_by_id(id)
        if err:
            raise Exception(err)
        if review:
            return ReviewType(**review)
        return None

# Mutations
class CreateReview(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        movie_id = graphene.Int(required=True)
        comment = graphene.String(required=True)
        rating = graphene.Int(required=True)

    review = graphene.Field(ReviewType)

    def mutate(self, info, user_id, movie_id, comment, rating):
        review_id, err = Review.create(user_id, movie_id, comment, rating)
        if err:
            raise Exception(err)
        review, _ = Review.get_by_id(review_id)
        return CreateReview(review=ReviewType(**review))

class UpdateReview(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        comment = graphene.String()
        rating = graphene.Int()

    review = graphene.Field(ReviewType)

    def mutate(self, info, id, comment=None, rating=None):
        err = Review.update(id, comment, rating)
        if err:
            raise Exception(err)
        review, _ = Review.get_by_id(id)
        return UpdateReview(review=ReviewType(**review))

class DeleteReview(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        err = Review.delete(id)
        if err:
            raise Exception(err)
        return DeleteReview(ok=True)

class Mutation(graphene.ObjectType):
    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()
    delete_review = DeleteReview.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)