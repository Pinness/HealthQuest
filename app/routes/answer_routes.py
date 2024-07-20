@app.route('/questions/<int:question_id>/answers', methods=['POST'])
    """
    Adds a new answer to a specific question.
    Purpose: Allows users to provide possible answers for a question in a quiz.
    User Experience Users submit answer details (text and correctness) through a form or API call.
    """
def add_answer(question_id):
    # Business logic to add an answer to a question



@app.route('/questions/<int:question_id>/answers', methods=['GET'])
    """
    Retrieves all answers for a specific question.
    Purpose: Displays a list of answers associated with a particular question in a quiz.
    User Experience**: Users view all possible answers for a question, typically for review or selection.
    """
def get_answers(question_id):
    # Business logic to get all answers for a question



@app.route('/answers/<int:answer_id>', methods=['GET'])
"""
    Retrieves details of a single answer.
    Purpose: Provides detailed information about a specific answer.
    User Experience: Users can view the text and correctness status of an individual answer.
    """
def get_answer(answer_id):
    # Business logic to get a single answer



@app.route('/answers/<int:answer_id>', methods=['PUT'])
    """
    Updates an existing answer.
    Purpose: Allows modification of the text or correctness of an answer.
    User Experience: Users can edit answer details through a form or API call to update the answer information.
    """
def update_answer(answer_id):
    # Business logic to update an answer



@app.route('/answers/<int:answer_id>', methods=['DELETE'])
    """
    Deletes a specific answer.
    Purpose: Removes an answer from the system.
    User Experience: Users can delete an answer, typically through an API call or interface action, removing it from the question.
    """
def delete_answer(answer_id):
    # Business logic to delete an answer
