import uvicorn
from fhir.resources.fhirtypes import Id
from fhir.resources.patient import Patient
from fhirstarter import FHIRProvider, FHIRStarter, InteractionContext
from fhirstarter.exceptions import FHIRResourceNotFoundError

# Create the main application
app = FHIRStarter()

# Create a provider to handle FHIR interactions
provider = FHIRProvider()

# Define a handler for reading patient data
@provider.read(Patient)
async def patient_read(context: InteractionContext, id_: Id) -> Patient:
    # This is where you'd typically implement your database lookup
    # For now, we'll return a simple example or raise not found
    if id_ == "example":
        return Patient(
            id=id_,
            active=True,
            name=[{"family": "Smith", "given": ["John"]}]
        )
    raise FHIRResourceNotFoundError

# Register the provider with the application
app.add_providers(provider)

if __name__ == "__main__":
    # Start the server with uvicorn, using module path notation
    uvicorn.run("fhirstarter.main:app")