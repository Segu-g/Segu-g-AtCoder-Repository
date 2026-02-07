from typing import TypedDict, Literal, Union
import logging
from pprint import pformat
logging.basicConfig(level=logging.INFO)

class SquareSegment(TypedDict):
    id: int
    base: list[int]
    size: list[int]
    connected: set[int]

def judge_pos(segment: SquareSegment, c: Literal["X", "Y"], a: int, b: int) -> Literal["L", "M", "U"]:
    direction = 0 if c == "X" else 1
    if a <= segment["base"][direction]:
        return "U"
    elif segment["base"][direction] + segment["size"][direction] <= a:
        return "L"
    else:
        return "M"
    
def is_connected(segment1: SquareSegment, segment2: SquareSegment):
    # 要素を入れ替えて接する位置関係を網羅する
    for segment_a, segment_b in ((segment1, segment2), (segment2, segment1)):
        # 横と縦で接する方向を入れ替える
        for direction in (0, 1):
            subdirection = 1 - direction
            # aが小さい（左か下）の断片
            a_upper = segment_a["base"][direction] + segment_a["size"][direction]
            # bが大きい（右か上）の断片
            b_lower = segment_b["base"][direction]
            # 辺の垂直方向の位置が一致している
            if a_upper == b_lower:
                a_upper_range = (segment_a["base"][subdirection], segment_a["base"][subdirection] + segment_a["size"][subdirection])
                b_lower_range = (segment_b["base"][subdirection], segment_b["base"][subdirection] + segment_b["size"][subdirection])
                # 辺の範囲に重なりがある
                if (a_upper_range[0] < b_lower_range[1]) and (b_lower_range[0] < a_upper_range[1]):
                    return True
    return False

def uf_root(uf: dict[int, int], x: int):
    value = uf[x]
    if value < 0:
        return x
    else:
        x_root = uf_root(uf, value)
        uf[x] = x_root
        return x_root
    
def uf_connect(uf: dict[int, int], x: int, y: int):
    x_root = uf_root(uf, x)
    y_root = uf_root(uf, y)
    if x_root == y_root:
        return
    x_root, y_root = sorted((x_root, y_root))
    uf[x_root] += uf[y_root]
    uf[y_root] = x_root

def main():
    n, x, y = map(int, input().split())
    queries = tuple(input().split() for _ in range(n))

    initial_segments = SquareSegment(id=0, base=[0, 0], size=[x, y], connected=set())
    
    square_segments: list[SquareSegment] = [initial_segments]
    current_square_segments = [initial_segments] 

    logging.debug("\n" + pformat(current_square_segments, width=120))
    for c, a, b in queries:
        a, b = int(a), int(b)
        direction = 0 if c == "X" else 1
        subdirection = 1 - direction

        # categorize by the position of segment
        lower_segments: list[SquareSegment] = []
        upper_segments: list[SquareSegment] = []
        middle_segments: list[SquareSegment] = []
        for segment in current_square_segments:
            next_pos = judge_pos(segment, c, a, b)
            if next_pos == "U":
                upper_segments.append(segment)
            elif next_pos == "L":
                lower_segments.append(segment)
            elif next_pos == "M":
                middle_segments.append(segment)

        # split middle segment
        for segment in middle_segments:
            lower_segment = SquareSegment(
                id=len(square_segments),
                base=segment["base"].copy(),
                size=segment["size"].copy(),
                connected=set()
            )
            square_segments.append(lower_segment)
            lower_segment["size"][direction] = a - segment["base"][direction]

            upper_segment = SquareSegment(
                id=len(square_segments),
                base=segment["base"].copy(),
                size=segment["size"].copy(),
                connected=set()
            )
            square_segments.append(upper_segment)
            upper_segment["base"][direction] = a
            upper_segment["size"][direction] = segment["size"][direction] - lower_segment["size"][direction]
            
            for connected_id in segment["connected"].copy():
                connected_segment = square_segments[connected_id]
            
                connected_segment["connected"].remove(segment["id"])
                segment["connected"].remove(connected_segment["id"])

                connected_segment["connected"].add(lower_segment["id"])
                lower_segment["connected"].add(connected_segment["id"])

                connected_segment["connected"].add(upper_segment["id"])
                upper_segment["connected"].add(connected_segment["id"])

            lower_segments.append(lower_segment)
            upper_segments.append(upper_segment)


        # shift all segment
        for lower_segment in lower_segments:
            lower_segment["base"][subdirection] -= b
        for upper_segment in upper_segments:
            upper_segment["base"][subdirection] += b

        # pick edge elements 
        lower_edge_segments = []
        upper_edge_segments = []
        for lower_segment in lower_segments:
            upper = lower_segment["base"][direction] + lower_segment["size"][direction]
            if upper == a:
                lower_edge_segments.append(lower_segment)
        for upper_segment in upper_segments:
            upper = upper_segment["base"][direction]
            if upper == a:
                upper_edge_segments.append(upper_segment)
        
        edge_segments: list[tuple[Literal["L", "U"], SquareSegment]] = [("L", segment) for segment in lower_edge_segments] + [("U", segment) for segment in upper_edge_segments]
        edge_segments.sort(key=lambda arg: arg[1]["base"][subdirection])
        current_lower_edge_segment: Union[SquareSegment, None] = None
        current_upper_edge_segment: Union[SquareSegment, None] = None
        for (label, segment) in edge_segments:
            # connect segments at edge
            if label == "L":
                current_lower_edge_segment = segment
            elif label == "U":
                current_upper_edge_segment = segment
            if current_lower_edge_segment is not None \
            and current_upper_edge_segment is not None:
                current_lower_edge_segment["connected"].add(current_upper_edge_segment["id"])
                current_upper_edge_segment["connected"].add(current_lower_edge_segment["id"])
        
        current_square_segments = lower_segments + upper_segments 
        for segment in current_square_segments:
            for connected_id in segment["connected"].copy():
                connected_segment = square_segments[connected_id]
                if not is_connected(segment, connected_segment):
                    segment["connected"].remove(connected_segment["id"])
                    connected_segment["connected"].remove(segment["id"])
        
        logging.debug("\n" + pformat(current_square_segments, width=120))

    uf: dict[int, int] = dict()
    segment_id_set = set()
    for segment in current_square_segments:
        uf[segment["id"]] = - (segment["size"][0] * segment["size"][1])
        segment_id_set.add(segment["id"])

    for segment_id in segment_id_set:
        segment = square_segments[segment_id]
        for connected_id in segment["connected"]:
            uf_connect(uf, segment_id, connected_id)
    root_segment_id_set = set()
    for segment_id in segment_id_set:
        root_segment_id_set.add(uf_root(uf, segment_id))
    
    connected_elements = [- uf[root_segment_id] for root_segment_id in root_segment_id_set]
    connected_elements.sort()
    print(len(connected_elements))
    print(" ".join(map(str, connected_elements)))


if __name__ == "__main__":

    main()
