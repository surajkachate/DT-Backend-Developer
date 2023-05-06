# Hello my name is Suraj Kachate I have created API using Python-Flask.
# API Creation

from flask import Flask, jsonify, request

app = Flask(__name__)


class Event:
    def __init__(self, uid, name, tagline, schedule, description, image, moderator, category, sub_category, rigor_rank, attendees):
        self.uid = uid
        self.name = name
        self.tagline = tagline
        self.schedule = schedule
        self.description = description
        self.image = image
        self.moderator = moderator
        self.category = category
        self.sub_category = sub_category
        self.rigor_rank = rigor_rank
        self.attendees = attendees

    def __repr__(self):
        return f"Event(uid={self.uid!r}, name={self.name!r}, tagline={self.tagline!r}, schedule={self.schedule!r}, description={self.description!r}, image={self.image!r}, moderator={self.moderator!r}, category={self.category!r}, sub_category={self.sub_category!r}, rigor_rank={self.rigor_rank!r}, attendees={self.attendees!r})"


#Empty array
events = []


# GET Events
@app.route('/api/v3/app/events', methods=['GET'])
def get_event():
    event_id = request.args.get('id')
    event_type = request.args.get('type')
    limit = request.args.get('limit')
    page = request.args.get('page')

    # Define API endpoint for getting an event by its id
    if event_id:
        for event in events:
            if str(event.uid) == event_id:
                return jsonify(event.__dict__)
        return jsonify({'error': 'Event not found'})

    # Define API endpoint for getting events by recency and pagination
    elif event_type and limit and page:
        limit = int(limit)
        page = int(page)

        # Sort events by recency
        if event_type == 'latest':
            sorted_events = sorted(events, key=lambda x: x.schedule, reverse=True)
        else:
            sorted_events = events

        # Paginate results
        start = (page - 1) * limit
        end = start + limit
        paginated_events = sorted_events[start:end]

        # Convert events to dictionary format
        result = []
        for event in paginated_events:
            event_dict = {
                'uid': event.uid,
                'name': event.name,
                'tagline': event.tagline,
                'schedule': event.schedule,
                'description': event.description,
                'image': event.image,
                'moderator': event.moderator,
                'category': event.category,
                'sub_category': event.sub_category,
                'rigor_rank': event.rigor_rank,
                'attendees': event.attendees
            }
            result.append(event_dict)

        return jsonify(result)


# POST Events
@app.route('/api/v3/app/events', methods=['POST'])
def create_event():
    # Get the request data as a dictionary
    data = request.form.to_dict()

    # Generate a new uid for the event
    uid = len(events) + 1

    # Create a new Event object
    event = Event(uid=uid,
                  name=data.get('name'),
                  tagline=data.get('tagline'),
                  schedule=data.get('schedule'),
                  description=data.get('description'),
                  image=data.get('files[image]'),
                  moderator=data.get('moderator'),
                  category=data.get('category'),
                  sub_category=data.get('sub_category'),
                  rigor_rank=data.get('rigor_rank'),
                  attendees=data.get('attendees'))

    # Add the new event to the events list
    events.append(event)

    # Return the uid of the new event
    return jsonify({'uid': uid})


# Define a function to create a new Event instance with default values
def get_default_event():
    return Event(uid=None, name='New Event', tagline='Hello', schedule=None, description='My name is Suraj Kachate', image=None, moderator='Yes', category='Backend Develper', sub_category='dotnet', rigor_rank=0, attendees=[])


# UPDATE Events
@app.route('/api/v3/app/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    # Find the event with the given id
    event = next((event for event in events if event.uid == event_id), None)

    # If the event doesn't exist, return a 404 error
    if event is None:
        return jsonify({'error': 'Event not found'}), 404

    # Create a new Event instance with default values
    default_event = get_default_event()

    # Update the event with the new instance
    event.name = default_event.name
    event.tagline = default_event.tagline
    event.schedule = default_event.schedule
    event.description = default_event.description
    event.image = default_event.image
    event.moderator = default_event.moderator
    event.category = default_event.category
    event.sub_category = default_event.sub_category
    event.rigor_rank = default_event.rigor_rank
    event.attendees = default_event.attendees

    # Return the updated event
    return jsonify(event.__dict__)



# DELETE Events
@app.route('/api/v3/app/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    # Find the event with the given id
    event = next((event for event in events if event.uid == event_id), None)

    # If the event doesn't exist, return a 404 error
    if event is None:
        return jsonify({'error': 'Event not found'}), 404

    # Remove the event from the list
    events.remove(event)

    # Return a success message
    return jsonify({'message': 'Event deleted successfully'})


# RUN
if __name__ == '__main__':
    app.run()



# create_event
# http://localhost:5000/api/v3/app/events

# get_event
# http://localhost:5000/api/v3/app/events?id=:event_id

# get_events
# http://localhost:5000/api/v3/app/events?type=latest&limit=5&page=1

# update_event
# http://localhost:5000/api/v3/app/events/:id

# delete_event
# http://localhost:5000/api/v3/app/events/:id