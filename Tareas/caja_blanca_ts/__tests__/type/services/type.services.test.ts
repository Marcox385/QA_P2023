import {expect, jest, test} from '@jest/globals';
import { TriangleDto } from '../../../type/dto/triangle.dto';
import typeService from '../../../type/services/type.service';

test('test triangle service isosceles', () => {

    const triangleDto1: TriangleDto = {
        sideA: 2, 
        sideB: 2,
        sideC: 1,
    };
    
    typeService.getTriangleType(triangleDto1).then(triangleType => {
        expect(triangleType).toBe('ISOSCELES');
    });

    const triangleDto2: TriangleDto = {
        sideA: 2, 
        sideB: 2,
        sideC: 2,
    };
    
    typeService.getTriangleType(triangleDto2).then(triangleType => {
        expect(triangleType).toBe('EQUILATERAL');
    });

    const triangleDto3: TriangleDto = {
        sideA: 2, 
        sideB: 3,
        sideC: 4,
    };
    
    typeService.getTriangleType(triangleDto3).then(triangleType => {
        expect(triangleType).toBe('SCALENE');
    });
    
});