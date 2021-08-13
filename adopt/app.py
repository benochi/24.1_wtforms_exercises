from flask import Flask, render_template, redirect, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "shh"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()
toolbar = DebugToolbarExtension(app)

@app.route("/")
def all_pets():
    ""'shows all pets"""
    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet"""

    form = AddPetForm()
    if form.validate_on_submit(): #converts googles 'y' string to a boolean using wtforms. 
        #can also do:
        # data = {k: v for k, v in form.data.items() if k != "csrf_token"}
        #new_pet = Pet(**data)
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data

        pet = Pet(
        name=name,
        species=species,
        photo_url=photo_url, 
        age=age, 
        notes=notes, 
        available=available
        )
 
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} has been added.")
        return redirect(url_for('all_pets'))
    else:
        return render_template("pet_add_form.hmtl", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet) #obj=variable name must match

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        flash(f"{pet.name} updated.")
        return redirect(url_for('all_pets'))

    else:
        # failed; re-present form for editing
        return render_template("pet_edit_form.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return info about pet converted to JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)