import pytest
from Superhero import func_for_heroes




class TestFunc:
        def test_success_with_job_true_and_male(serf):
                
                result = func_for_heroes(True, "Male")
                assert isinstance(result, str)

        def test_success_with_job_true_and_female(self):
       
                result = func_for_heroes(True, "Female")
                assert isinstance(result, str)
        
        def test_success_with_job_true_and_dash(self):
                
                result = func_for_heroes(True, "-")
                assert isinstance(result, str)
                
        def test_success_with_job_false_and_male(self):
               
                result = func_for_heroes(False, "Male")
                assert isinstance(result, str)   

        def test_success_with_job_false_and_female(self):
               
                result = func_for_heroes(False, "Female")
                assert isinstance(result, str)

        def test_success_with_job_false_and_tire(self):
        
                result = func_for_heroes(False, "-")
                assert isinstance(result, str)

        @pytest.mark.parametrize(
        "invalid_gender",
        [
                "",
                "male",
                "female",
                "FEMALE",
                "MALE",
                " - ",  
                "123",
                "None",
                "!@#$%^&*()_-" 
        ]
    )
    
        def test_invalid_gender_raises_error(self, invalid_gender):

                with pytest.raises(UnboundLocalError):

                        func_for_heroes(True, invalid_gender)

        @pytest.mark.parametrize(
        "invalid_job",
        [
                " ",
                "t",
                "0",  
                "1",
                "!@#$%^&*()_-" 
        ]
    )
        def test_invalid_boolean_raises_error(serf, invalid_job):

                with pytest.raises(UnboundLocalError):
                        func_for_heroes(invalid_job, "Male")
        
        def test_null_boolean_raises_error(serf):

                with pytest.raises(TypeError):
                        func_for_heroes()


