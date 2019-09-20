#class for review in prime events

class Review:
    #to keep track of number of objects
    numOfReviews = 0
    #review id to be generated
    reviewId = 0

    def __init__(self, hallId, userId, reviewDate, rating, comment):
        self.hallId = hallId
        self.userId = userId
        self.reviewDate = reviewDate
        self.rating = rating
        self.comment = comment
        Review.numOfReviews += 1

    def getHallId(self):
        return self.hallId

    def getUserId(self):
        return self.userId

    def getReviewDate():
        return self.reviewDate

    def getReviewId():
        return self.reviewId
    
    def getRating():
        return self.rating

    def provideReview():
        #auto-generate review id in the database on confirmation of payment
        #once review id is fetched then review entry is added in the database
        #get the existing sequence number and append 1 to it.
        pass

    def getNumOfReviewObjectsCreated():
        return Review.numOfUsers



