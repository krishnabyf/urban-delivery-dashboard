from fastapi import FastAPI

app = FastAPI()

# Sample Data (simulate government program)
cities = [
    {"name": "Hyderabad", "jobs_completed": 120, "delays": 5},
    {"name": "Mumbai", "jobs_completed": 200, "delays": 20},
    {"name": "Delhi", "jobs_completed": 150, "delays": 10},
]

@app.get("/")
def home():
    return {"message": "Urban Delivery Dashboard API Running"}

@app.get("/cities")
def get_cities():
    return cities

@app.get("/metrics")
def get_metrics():
    total_jobs = sum(city["jobs_completed"] for city in cities)
    total_delays = sum(city["delays"] for city in cities)

    return {
        "total_jobs": total_jobs,
        "total_delays": total_delays
    }
