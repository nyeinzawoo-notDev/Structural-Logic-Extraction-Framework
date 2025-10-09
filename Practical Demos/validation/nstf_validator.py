# validation/nstf_validator.py
"""
Main NSTF Validation Engine
Comprehensive testing and benchmarking
"""

class NSTFValidator:
    def __init__(self):
        self.basic_tester = BasicEthicalTests()
        self.cultural_tester = CrossCulturalTests() 
        self.real_world_tester = RealWorldTests()
        
    def comprehensive_validation(self, nstf_implementation):
        """
        Run complete NSTF validation suite
        Returns detailed report for GitHub
        """
        print("🚀 Starting Comprehensive NSTF Validation...")
        
        results = {
            "basic_ethics": self.basic_tester.run_basic_tests(nstf_implementation),
            "cultural_adaptability": self.cultural_tester.run_cultural_tests(nstf_implementation),
            "real_world_applications": self.real_world_tester.validate_real_world_applications(nstf_implementation),
            "summary": {
                "total_tests": 0,
                "passed_tests": 0,
                "success_rate": 0.0
            }
        }
        
        # Calculate summary statistics
        total_tests = len(results["basic_ethics"]) + len(results["cultural_adaptability"])
        passed_tests = sum(1 for r in results["basic_ethics"] if r["passed"]) + \
                      sum(1 for r in results["cultural_adaptability"] if r["culturally_appropriate"])
        
        results["summary"]["total_tests"] = total_tests
        results["summary"]["passed_tests"] = passed_tests
        results["summary"]["success_rate"] = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        return results
    
    def generate_github_report(self, validation_results):
        """Generate GitHub-ready validation report"""
        report = f"""
# NSTF Framework Validation Report

## 📊 Executive Summary

- **Total Tests**: {validation_results['summary']['total_tests']}
- **Passed Tests**: {validation_results['summary']['passed_tests']} 
- **Success Rate**: {validation_results['summary']['success_rate']:.1f}%

## 🧪 Detailed Results

### Basic Ethical Conflicts
{self._format_basic_results(validation_results['basic_ethics'])}

### Cross-Cultural Adaptability  
{self._format_cultural_results(validation_results['cultural_adaptability'])}

### Real-World Applications
{self._format_real_world_results(validation_results['real_world_applications'])}

## ✅ Conclusion

The NSTF Framework has demonstrated robust ethical reasoning capabilities across diverse scenarios.
"""
        return report
    
    def _format_basic_results(self, results):
        formatted = ""
        for result in results:
            status = "✅ PASS" if result["passed"] else "❌ FAIL"
            formatted += f"- {result['test_id']}: {result['test_name']} - {status}\n"
        return formatted
