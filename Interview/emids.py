
import json
emids = {
  "hospital": {
    "name": "Green Valley Medical Center",
    "location": {
      "address": {
        "street": "456 Wellness Way",
        "city": "MediTown",
        "state": "CA",
        "zip": "90210"
      },
      "coordinates": {
        "latitude": 34.0901,
        "longitude": -118.4065
      }
    },
    "departments": [
      {
        "name": "Cardiology",
        "head": "Dr. Alice Monroe",
        "staff": [
          { "id": "D101", "name": "Dr. Alice Monroe", "role": "Cardiologist" },
          { "id": "N102", "name": "Nurse James", "role": "Registered Nurse" }
        ]
      },
      {
        "name": "Neurology",
        "head": "Dr. Brian Jacobs",
        "staff": [
          { "id": "D103", "name": "Dr. Brian Jacobs", "role": "Neurologist" }
        ]
      }
    ],
    "patients": [
      {
        "id": "P10001",
        "personalInfo": {
          "firstName": "Emily",
          "lastName": "Clark",
          "gender": "Female",
          "dob": "1990-02-18",
          "contact": {
            "phone": "+1-555-678-1234",
            "email": "emily.clark@example.com"
          },
          "address": {
            "street": "789 Patient Ln",
            "city": "CareCity",
            "state": "CA",
            "zip": "90001"
          }
        },
        "insurance": {
          "provider": "SecureHealth",
          "policyNumber": "SH123456789",
          "validThrough": "2026-12-31"
        },
        "visits": [
          {
            "visitId": "V20240601",
            "date": "2024-06-01",
            "department": "Cardiology",
            "reason": "Chest pain",
            "doctor": "Dr. Alice Monroe",
            "diagnosis": "Mild Angina",
            "labResults": {
              "ECG": {
                "result": "Abnormal",
                "notes": "Irregular rhythm detected",
                "date": "2024-06-01"
              },
              "BloodTest": {
                "CBC": {
                  "WBC": 6.3,
                  "RBC": 4.7,
                  "Hemoglobin": 13.9,
                  "Platelets": 250
                },
                "LipidProfile": {
                  "TotalCholesterol": 210,
                  "HDL": 40,
                  "LDL": 160,
                  "Triglycerides": 180
                },
                "date": "2024-06-01"
              }
            },
            "prescriptions": [
              {
                "medication": "Atenolol",
                "dosage": "50mg",
                "frequency": "Once daily",
                "duration": "30 days"
              }
            ],
            "billing": {
              "totalAmount": 450.00,
              "coveredByInsurance": 300.00,
              "patientResponsibility": 150.00,
              "invoiceId": "INV-45678"
            },
            "careTeam": {
              "primaryDoctor": "Dr. Alice Monroe",
              "nurses": ["Nurse James"],
              "consults": ["Dr. Brian Jacobs"]
            }
          }
        ]
      }
    ]
  }
}
from flatten_json import flatten

flat_json = flatten(emids)

print(flat_json)
# print(emids.get("hospital").get("location"))
# len = len(emids)
# for k, v in emids.items():
#     # print(f"key:"{k}, "value"{v}"}
#     if len(k)>1:
#         for k, v in emids.items():
#             print(f"key:{k} value: {v}")

