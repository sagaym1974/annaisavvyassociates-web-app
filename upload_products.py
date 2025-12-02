import firebase_admin
from firebase_admin import credentials, firestore
import json

# Initialize Firebase Admin SDK with your service account key file.
cred = credentials.Certificate("serviceAccountKey.json")
if not firebase_admin._apps:  # Avoid multiple initializations
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Load your product catalog JSON file.
with open("products_catalog.json", encoding='utf-8') as f:
    products = json.load(f)

# Build set of filenames currently in your JSON
current_filenames = set()
for product in products:
    fname = product.get("filename")
    if fname:
        current_filenames.add(fname)

# Delete Firestore docs not in your latest product list
collection_ref = db.collection("products_catalog")
for doc in collection_ref.stream():
    if doc.id not in current_filenames:
        print(f"Deleting obsolete product: {doc.id}")
        doc.reference.delete()

# Upload/update Firestore docs for all current products
for product in products:
    doc_id = product.get("filename", None)
    if doc_id:
        collection_ref.document(doc_id).set(product)
    else:
        collection_ref.add(product)

print("Sync complete. Firestore now matches products_catalog.json.")
