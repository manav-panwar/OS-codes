# Page Replacement Policies: LRU, FIFO, Optimal

def lru(page_sequence, frame_size):
    frames = []
    page_faults = 0

    for page in page_sequence:
        if page not in frames:
            page_faults += 1
            if len(frames) == frame_size:
                # Remove the least recently used page
                frames.pop(0)
        else:
            # Remove the page and reinsert to mark it as recently used
            frames.remove(page)
        frames.append(page)
        print(f"Page: {page}, Frames: {frames}")

    print(f"Total LRU Page Faults: {page_faults}")
    return page_faults


def fifo(page_sequence, frame_size):
    frames = []
    page_faults = 0

    for page in page_sequence:
        if page not in frames:
            page_faults += 1
            if len(frames) == frame_size:
                # Remove the first page in the frames (FIFO)
                frames.pop(0)
        frames.append(page)
        print(f"Page: {page}, Frames: {frames}")

    print(f"Total FIFO Page Faults: {page_faults}")
    return page_faults


def optimal(page_sequence, frame_size):
    frames = []
    page_faults = 0

    for i in range(len(page_sequence)):
        page = page_sequence[i]
        if page not in frames:
            page_faults += 1
            if len(frames) == frame_size:
                # Find the page to replace (used farthest in the future or not used at all)
                future_indices = [page_sequence[i + 1:].index(f) if f in page_sequence[i + 1:] else float('inf') for f in frames]
                replace_index = future_indices.index(max(future_indices))
                frames.pop(replace_index)
            frames.append(page)
        print(f"Page: {page}, Frames: {frames}")

    print(f"Total Optimal Page Faults: {page_faults}")
    return page_faults


# Main function
if __name__ == "__main__":
    # Input page sequence and frame size
    page_sequence = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    frame_size = 3

    print("\n--- LRU (Least Recently Used) ---")
    lru(page_sequence, frame_size)

    print("\n--- FIFO (First-In-First-Out) ---")
    fifo(page_sequence, frame_size)

    print("\n--- Optimal Page Replacement ---")
    optimal(page_sequence, frame_size)
