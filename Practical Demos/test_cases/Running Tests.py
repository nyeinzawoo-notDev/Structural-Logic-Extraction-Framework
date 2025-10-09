from validation.nstf_validator import NSTFValidator

validator = NSTFValidator()
results = validator.comprehensive_validation(your_nstf_implementation)
print(validator.generate_github_report(results))
